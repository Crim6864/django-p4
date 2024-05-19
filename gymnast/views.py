from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from .models import Gymnast
from .forms import GymnastForm

class AddGymnastView(LoginRequiredMixin, CreateView):
    template_name = 'gymnast/add_gymnast.html'
    form_class = GymnastForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.parent1 = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['second_parent'] = self.get_second_parent()
        return context

    def get_second_parent(self):
        return User.objects.filter(is_superuser=True).first()

class EditGymnastView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "gymnast/edit_gymnast.html"
    form_class = GymnastForm
    model = Gymnast

    def get_object(self, queryset=None):
        return get_object_or_404(Gymnast, pk=self.kwargs['pk'])

    def test_func(self):
        gymnast = self.get_object()
        return self.request.user == gymnast.user

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})

class DeleteGymnastView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Gymnast
    template_name = 'gymnast/delete_gymnast.html'
    context_object_name = 'gymnast'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})

    def test_func(self):
        return self.request.user.is_superuser

class MoveGymnastView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Gymnast
    form_class = GymnastForm
    template_name = 'gymnast/move_gymnast.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})

    def test_func(self):
        return self.request.user.is_superuser

class ViewGymnastView(LoginRequiredMixin, ListView):
    model = Gymnast
    template_name = 'gymnast/gymnast_list.html'
    context_object_name = 'gymnasts'

    def get_queryset(self):
        return Gymnast.objects.filter(user=self.request.user)