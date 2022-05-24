import os
import pathlib
import requests
from flask import Flask, url_for, redirect, session, abort
from flask_restful import Api
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
from resources.cuisine import *
from resources.menus import MenuList
from resources.cuisinerecipe import *
from resources.recipedetails import RecipeDetails

setup()  # connect to db and creates necessary tables.

app = Flask(__name__)
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # OAuth acces
app.secret_key = '!secret'
api = Api(app)

GOOGLE_CLIENT_ID = "69465386927-uov5kn1vgopkp818ro01qjmkgfrttnso.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")
flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email",
            "openid"],
    redirect_uri="http://127.0.0.1:5000/authorize"
)


# decorator to check if login is required
def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Auth Required
        else:
            return function()

    return wrapper


# Home Page
@app.route('/')
def index():
    return "Welcome Food Court !!"


# Plans page Login required
@app.route('/plans')
@login_is_required
def plans():
    return redirect('/menus')


# login page
@app.route('/login')
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)

# callback page
@app.route('/authorize')
def authorize():
    flow.fetch_token(authorization_response=request.url)
    if not session["state"] == request.args["state"]:
        abort(500)  # Unmatched State

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )
    session["google_id"] = id_info.get("sub")  # defing the results to show on the page
    session["name"] = id_info.get("name")

    return redirect("/plans")

# clear session and logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


# Resources
api.add_resource(Cuisine, '/cuisine/<string:name>')
api.add_resource(CuisineList, '/cuisines')
api.add_resource(CuisineRecipes, '/cuisine/<string:name>/recipes')
api.add_resource(RecipeDetails, '/cuisine/<string:cui_name>/recipe/<int:rec_id>')

api.add_resource(MenuList, '/menus')

app.run(port=5000, debug=True)
