from urllib import request
from jose import jwt
from social_core.backends.oauth import BaseOAuth2


class AAD(BaseOAuth2):
    """AAD OAuth authentication backend"""
    name = 'aad'
    SCOPE_SEPARATOR = ' '
    ACCESS_TOKEN_METHOD = 'POST'
    REDIRECT_STATE = False

    def authorization_url(self):
        return 'https://login.microsoftonline.com/' + self.setting('DOMAIN') + '/oauth2/v2.0/authorize'

    def access_token_url(self):
        return 'https://login.microsoftonline.com/' + self.setting('DOMAIN') + '/oauth2/v2.0/token'

    def get_user_id(self, details, response):
        """Return current user id."""
        return details['preferred_username']

    def get_user_details(self, response):
        id_token = response.get('id_token')
        print(id_token)
        jwks = request.urlopen('https://login.microsoftonline.com/' + self.setting('DOMAIN') + '/discovery/v2.0/keys')
        issuer = 'https://login.microsoftonline.com/' + self.setting('DOMAIN') + '/v2.0'
        audience = self.setting('KEY')  # CLIENT_ID
        payload = jwt.decode(id_token, jwks.read(), algorithms=['RS256'], audience=audience, issuer=issuer)
        payload["fullname"] = payload["name"]
        payload["first_name"] = payload["name"]
        payload["username"] = payload["preferred_username"]
        return payload