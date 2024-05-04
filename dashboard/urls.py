# dashboard/urls.py
from django.urls import path
from .views import Profile

app_name = 'dashboard'

urlpatterns = [
    path('profile/', Profile.as_view(), name='profile'),
]
