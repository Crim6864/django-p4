from django.urls import path
from .views import Index, Traning, Contact, Om, Calender

urlpatterns = [
    path("", Index.as_view(), name="home"),
    path("traning", Traning.as_view(), name="traning"),
    path("contact", Contact.as_view(), name="contact"),
    path("om", Om.as_view(), name="om"),
    path("calender", Calender.as_view(), name="calender"),
]
