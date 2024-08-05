from rest_framework.authentication import TokenAuthentication, get_authorization_header


class MyTokenAuthentication(TokenAuthentication):
    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        print("AA"*10)
        print(auth)
        return super().authenticate(request)