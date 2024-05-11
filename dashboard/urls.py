from django.urls import path
from .views import UserDashboardView, AdminDashboardView

urlpatterns = [
    path('user_dashboard/', UserDashboardView.as_view(), name='user_dashboard'),
    path('admin_dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
]
