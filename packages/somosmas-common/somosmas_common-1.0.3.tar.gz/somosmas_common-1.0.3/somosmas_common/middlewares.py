from oauth2_provider.middleware import (
    OAuth2TokenMiddleware as ToolkitOAuth2TokenMiddleware
)


class OAuth2TokenMiddleware(ToolkitOAuth2TokenMiddleware):
    def process_request(self, request):
        if '/oauth2/inspect' not in request.path:
            super().process_request(request)