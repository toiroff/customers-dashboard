from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticaterd_user(view_func):
  def wrapper_func(request,*args, **kwargs):
      if request.user.is_authenticated:
        return redirect('home')
      else:
         return view_func(request,*args, **kwargs)
    
  return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            # Check if the group is in allowed roles
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not allowed to see this page')

        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.first().name  # It's more efficient to use first()

        if group == 'customer':
            return redirect('user-page')

        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_func
