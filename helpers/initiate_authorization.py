from google_auth_oauthlib.flow import Flow

def initiate_authorization(file_name, scopes, redirect_uri, **kwargs):
    # Use the client_secret.json file to identify the application requesting
    # authorization. The client ID (from that file) and access scopes are required.
    flow = Flow.from_client_secrets_file(file_name, scopes)

    # Indicate where the API server will redirect the user after the user completes
    # the authorization flow.
    flow.redirect_uri = redirect_uri

    # Generate URL for request to Google's OAuth 2.0 server.
    # Use kwargs to set optional request parameters.
    authorization_url, state = flow.authorization_url(
        # Enable offline access so that you can refresh an access token without
        # re-prompting the user for permission. Recommended for web server apps.
        access_type=kwargs.get('access_type', 'online'),
        # Enable incremental authorization. Recommended as a best practice.
        include_granted_scopes=kwargs.get('include_granted_scopes', 'false'),
        prompt='consent')
    
    return authorization_url, state