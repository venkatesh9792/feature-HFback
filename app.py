from authlib.integrations.flask_client import OAuth
from flask import Flask, url_for, redirect

from cuisine import *

# connect to db and creates necessary tables.
setup()

app = Flask(__name__)
api = Api(app)

app.secret_key = '!secret'
# oauth config
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='69465386927-uov5kn1vgopkp818ro01qjmkgfrttnso.apps.googleusercontent.com',
    client_secret='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',
    # access_token_url='',
    # access_token_params='',
    # authorize_url='',
    # authorize_params='',
    # api_base_url='',
    # client_kwargs=''
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid profile email'}

)


@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@app.route('/authorize')
def authorize():
    token = oauth.google.authorize_access_token()
    return redirect('/cuisines')


api.add_resource(Cuisine, '/cuisine/<string:name>')
api.add_resource(CuisineList, '/cuisines')

app.run(port=5000, debug=True)
