from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login


class LoginView(TemplateView):
    template_name = 'users/login.html'

class SignupView(TemplateView):
    template_name = 'users/signup.html'

class LogoutView(TemplateView):
    template_name = 'users/logout.html'



def ajax_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'redirect_url': '/dashboard/'})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid username or password.'})
    else:
        return JsonResponse({'success': False, 'error': 'Only POST requests are allowed.'})

