from helpers.fetch_events import fetch_events
from helpers.fetch_token import fetch_token
from helpers.initiate_authorization import initiate_authorization
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import webbrowser

data = {
    'client_secret' : 'client_secret.json',
    'scopes' : ['https://www.googleapis.com/auth/calendar.readonly'],
    'redirect_uri' : 'http://localhost:8080/rest/v1/calendar/redirect/'
}

class GoogleCalendarInitView(APIView):
    
    def get(self, request):

        try:
            # fetch authorization url
            authorization_url, state = initiate_authorization(
                data['client_secret'],
                data['scopes'],
                data['redirect_uri'],
                access_type='offline',
                include_granted_scopes='true')
        except:
            return Response(
                data="Unexpected Error, check server logs.",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        try:
            # for cross-client compatibilty, we use 'webbrowwer.open()'
            # instead of redirection.
            webbrowser.open(authorization_url, new=1, autoraise=True)
        except:
            # If client was unable to open browser, suggest the user
            # to manually open it.
            return Response(
                data="Open this url in your browser {}".format(authorization_url),
                status=status.HTTP_200_OK)
        # code will never reach here.
        return Response(status=status.HTTP_200_OK)

class GoogleCalendarRedirectView(APIView):
    
    def get(self, request):
        code = request.query_params['code']

        # Exchange 'access_token' and 'refresh_token' for
        # auth_code.
        try:
            credentials = fetch_token(
                data['client_secret'],
                data['scopes'],
                data['redirect_uri'],
                code=code)
        except:
            return Response(
                data="Unexpected Error, check server logs.",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Make a call to GoogleCalendarAPI to fetch events
        # list with their start-times.
        try:
            events = fetch_events(credentials)
        except:
            return Response(
                data="Failed to retrieve events list, check server logs.",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data=events, status=status.HTTP_200_OK)