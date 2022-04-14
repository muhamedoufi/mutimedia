from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse


def secretaire_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
       
        if group == 'secretaires':
			
            return view_func(request, *args, **kwargs)
        else: 
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
        # else:
        #     return # <- return response here (possibly a redirect to login page?)

    return wrapper_function