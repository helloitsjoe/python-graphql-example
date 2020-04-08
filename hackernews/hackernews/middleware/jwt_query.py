TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZseW50Zmxvc3N5NjkiLCJleHAiOjE1ODYxMzMwODQsIm9yaWdfaWF0IjoxNTg2MTMyNzg0fQ.jLJWFAueFmkl6224vR9lWK0gEyE9XpsIk-C_SUoPW1w"

class JWTQueryMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.GET.get('token'))
        token = request.GET.get('token', TOKEN)
        request.META['HTTP_AUTHORIZATION'] = 'JWT ' + token
        response = self.get_response(request)
        return response
