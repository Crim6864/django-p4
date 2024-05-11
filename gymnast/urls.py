from django.urls import path
from .views import AddGymnastView, EditGymnastView

urlpatterns = [
    path('add_gymnast/', AddGymnastView.as_view(), name='add_gymnast'),
    path('edit_gymnast/<int:pk>/', EditGymnastView.as_view(), name='edit_gymnast'),
]
