# from flask import Flask, render_template, url_for, redirect
# from authlib.integrations.flask_client import OAuth

# app = Flask(__name__)

# oauth = OAuth(app)

# app.config["SECRET_KEY"] = "THIS SHOULD BE SECRET"
# app.config["GITHUB_CLIENT_ID"] = "82a349f92850f23f12c3"
# app.config["GITHUB_CLIENT_SECRET"] = "55f9bf24e692b55ad7e6d07015975060c35af79b"


# github = oauth.register(
#     name="github",
#     client_id=app.config["GITHUB_CLIENT_ID"],
#     client_secret=app.config["GITHUB_CLIENT_SECRET"],
#     access_token_url="https://github.com/login/oauth/access_token",
#     access_token_params=None,
#     authorize_url="https://github.com/login/oauth/authorize",
#     authorize_params=None,
#     api_base_url="https://api.github.com/",
#     client_kwargs={"scope": "user:email"},
# )

# github = oauth.create_client("github")


# # Github login route
# @app.route("/login/github")
# def github_login():
#     redirect_uri = url_for("github_authorize", _external=True)
#     return github.authorize_redirect(redirect_uri)


# # Github authorize route
# @app.route("/login/github/authorize")
# def github_authorize():
#     token = github.authorize_access_token()
#     resp = github.get("user").json()
#     return redirect("/home")


# @app.route("/home")
# def home_page():
#     return "home"


# if __name__ == "__main__":
#     app.run(debug=True)
from requests_oauthlib import OAuth2Session

# GitHub OAuth configuration
client_id = "82a349f92850f23f12c3"
client_secret = "55f9bf24e692b55ad7e6d07015975060c35af79b"
authorization_base_url = "https://github.com/login/oauth/authorize"
token_url = "https://github.com/login/oauth/access_token"
redirect_uri = "http://localhost:8501/Dashboard"


def get_github_oauth_session():
    return OAuth2Session(client_id, redirect_uri=redirect_uri)


def github_login_url(oauth_session):
    return oauth_session.authorization_url(authorization_base_url)


def fetch_github_token(oauth_session, token_url, code, client_secret):
    return oauth_session.fetch_token(
        token_url, authorization_response=code, client_secret=client_secret
    )
