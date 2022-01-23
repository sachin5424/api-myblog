import json


def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # request.META.get['jj'] = "jhgfds"
        _mutable = request.GET._mutable
        request.GET._mutable = True
        request.GET['my_name'] = "sachin"
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = get_response(request)
        print(response)
        # Code to be executed for each request/response after
        # the view is called.
        return response

    return middleware