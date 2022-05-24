from client import get_cuisine


def test_get_cuisine():
    response = get_cuisine("indian")
    assert response['cuisine'] == "indian"
