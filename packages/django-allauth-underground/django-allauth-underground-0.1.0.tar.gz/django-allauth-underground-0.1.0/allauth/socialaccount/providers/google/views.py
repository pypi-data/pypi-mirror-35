import requests

from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import GoogleProvider


class GoogleOAuth2Adapter(OAuth2Adapter):
    provider_id = GoogleProvider.id
    access_token_url = 'https://accounts.google.com/o/oauth2/token'
    authorize_url = 'https://accounts.google.com/o/oauth2/auth'
    profile_url = 'https://www.googleapis.com/oauth2/v1/userinfo'
    people_url = 'https://people.googleapis.com/v1/people/me'

    def complete_login(self, request, app, token, **kwargs):
        resp = requests.get(self.profile_url,
                            params={'access_token': token.token,
                                    'alt': 'json'})
        resp.raise_for_status()
        extra_data = resp.json()
        
        # SOCIALACCOUNT_PROVIDERS scopes
        # 'google': {
        #     'SCOPE': [        
        #         'https://www.googleapis.com/auth/user.birthday.read',
        #         'https://www.googleapis.com/auth/userinfo.email',
        #         'https://www.googleapis.com/auth/userinfo.profile'
        #     ],
        # }
        
        _extra_data = requests.get(
            self.people_url + "?personFields=birthdays,coverPhotos,emailAddresses,names,taglines",
            params={'access_token': token.token, 'alt': 'json'}
        )
        people_data = _extra_data.json()
        extra_data['people'] = people_data
        
        login = self.get_provider() \
            .sociallogin_from_response(request,
                                       extra_data)
        return login


oauth2_login = OAuth2LoginView.adapter_view(GoogleOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(GoogleOAuth2Adapter)
