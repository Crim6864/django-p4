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
