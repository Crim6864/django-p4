from django.urls import path
from .views import Profile

urlpatterns = [
    path('user/<slug:pk>/', Profile.as_view(), name='profile'),
]
