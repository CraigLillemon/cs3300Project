from django.http import HttpResponse
from django.shortcuts import redirect
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            print('role', allowed_roles)
            group = None
            if request.user.group.exists():
                group = request.user.group.all()[0].name
                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse("You can't be here")
            return wrapper_func
        return decorator