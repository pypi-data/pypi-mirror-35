import requests
from django.conf import settings
from django.contrib.auth.models import User


class OAuthBackend:
    def authenticate(self, request, token=None):
        _token = request.META.get('HTTP_AUTHORIZATION')

        response = requests.post(
            settings.OAUTH_INTROSPECT_URL,
            headers={
                'Authorization': 'Bearer {}'.format(
                    settings.OAUTH_INTROSPECT_TOKEN
                )
            },
            data={
                'token': _token
            }
        ).json()

        if response['active']:
            user_data = requests.post(
                settings.OAUTH_BASE_URL + '/graphql/',
                data="""
                    query {
                        me {
                          id
                          username
                          firstName
                          lastName
                          email                        
                        }
                    }
                """,
                headers={
                    'Authorization: Bearer {}'.format(_token)
                }
            ).json()['data']
            return User(
                username=user_data['username'],
                first_name=user_data['firstName'],
                last_name=user_data['lastName'],
                email=user_data['email'],
            )
        else:
            return None
