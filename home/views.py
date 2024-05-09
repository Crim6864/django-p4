from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "home/index.html"


class Traning(TemplateView):
    template_name = "home/traning.html"


class Contact(TemplateView):
    template_name = "home/contact.html"


class Om(TemplateView):
    template_name = "home/om.html"


class Calender(TemplateView):
    template_name = "home/calender.html"
