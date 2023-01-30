from google_auth_oauthlib.flow import Flow

def fetch_token(file_name, scopes, redirect_uri, **kwargs):
    flow = Flow.from_client_secrets_file(file_name, scopes)
    flow.redirect_uri = redirect_uri

    # Fetch 'access_token' + 'refresh_token' using 'auth_code'.
    flow.fetch_token(code = kwargs.get("code"))

    # We will store the credentials in django-sessions.
    credentials = flow.credentials
    return credentials