from django.urls import path
from .views import ajax_login

urlpatterns = [
    path('ajax/login/', ajax_login, name='ajax_login'),
]
