
class ApiMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.META['CONTENT_TYPE'] == 'application/json':
            return "JSON!"

        return self.get_response(request)
