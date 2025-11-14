import requests
from social_core.backends.oauth import BaseOAuth2
from django.conf import settings

class Auth0(BaseOAuth2):
    name = 'auth0'
    SCOPE_SEPARATOR = " "
    ACCESS_TOKEN_METHOD = 'POST'
    EXTRA_DATA = [('picture', 'picture')]

    def authorization_url(self):
        return "https://" + self.setting('DOMAIN') + "/authorize"

    def access_token_url(self):
        return "https://" + self.setting('DOMAIN') + "/oauth/token"

    def get_user_id(self, details, response):
        return details['user_id']

    def get_user_details(self, response):
        url = 'https://' + self.setting('DOMAIN') + '/userinfo'
        headers = {'authorization': 'Bearer ' + response['access_token']}
        resp = requests.get(url, headers=headers)
        userinfo = resp.json()
        return {
            'username': userinfo.get('nickname'),
            'first_name': userinfo.get('name'),
            'picture': userinfo.get('picture'),
            'user_id': userinfo.get('sub')
        }

# Esta función está fuera de la clase
def getRole(request):
    user = request.user
    auth0user = user.social_auth.filter(provider="auth0")[0]
    accessToken = auth0user.extra_data['access_token']
    url = 'https://' + settings.SOCIAL_AUTH_AUTH0_DOMAIN + '/userinfo'
    headers = {'authorization': 'Bearer ' + accessToken}
    resp = requests.get(url, headers=headers)
    userinfo = resp.json()
    role = userinfo.get(f"{settings.SOCIAL_AUTH_AUTH0_DOMAIN}/role")
    return role
