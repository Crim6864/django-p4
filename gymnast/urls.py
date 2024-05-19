# gymnast/urls.py

from django.urls import path
from .views import AddGymnastView, EditGymnastView, DeleteGymnastView, MoveGymnastView, ViewGymnastView

urlpatterns = [
    path('add_gymnast/', AddGymnastView.as_view(), name='add_gymnast'),
    path('edit_gymnast/<int:pk>/', EditGymnastView.as_view(), name='edit_gymnast'),
    path('delete_gymnast/<int:pk>/', DeleteGymnastView.as_view(), name='delete_gymnast'),
    path('move_gymnast/<int:pk>/', MoveGymnastView.as_view(), name='move_gymnast'),
    path('view_gymnast/<int:pk>/', ViewGymnastView.as_view(), name='view_gymnast'),
]