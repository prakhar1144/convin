from helpers.initiate_authorization import initiate_authorization
from rest_framework.response import Response
from rest_framework.views import APIView
import webbrowser

class GoogleCalendarInitView(APIView):
    
    def get(self, request):
        client_secret = 'client_secret.json'
        scopes = ['https://www.googleapis.com/auth/calendar.readonly']
        redirect_uri = 'http://localhost:8080/rest/v1/calendar/redirect/'

        authorization_url, state = initiate_authorization(
            client_secret,
            scopes,
            redirect_uri,
            access_type='offline',
            include_granted_scopes='true')

        try:
            webbrowser.open(authorization_url, new=1, autoraise=True)
        except:
            return Response(data="Open this url in your browser {}".format(authorization_url))
        return Response(status=200)

class GoogleCalendarRedirectView(APIView):
    pass