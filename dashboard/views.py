from django.shortcuts import redirect, render
from django.views.generic import TemplateView

class Profile(TemplateView):
    template_name = 'dashboard/profile.html'
