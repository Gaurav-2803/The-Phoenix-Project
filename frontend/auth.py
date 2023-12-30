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


def fetch_github_token(oauth_session, code):
    return oauth_session.fetch_token(
        token_url, authorization_response=code, client_secret=client_secret
    )
