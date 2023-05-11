from django.shortcuts import redirect

class CustomAuthMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        print(f"user: {request.user.is_superuser}")
        if request.user.is_authenticated == False and request.path != '/admin/login/':
            return redirect('/admin/login/?next=' + request.path)
        return response

        
        