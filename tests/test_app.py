from secrets import token_hex


def test_app_is_created(app):
    assert app.name == "flaskblog"


def test_config_is_loaded(config):
    assert config["DEBUG"] is False


def test_request_returns_200(client):
    assert client.get("/").status_code == 200


def test_request_returns_404(client):
    assert client.get(f"/{token_hex()}").status_code == 404
