from django.views.generic import TemplateView, CreateView, UpdateView
from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .models import Gymnast
from .forms import GymnastForm

class AddGymnastView(LoginRequiredMixin, CreateView):
    template_name = 'gymnast/add_gymnast.html'
    form_class = GymnastForm
    success_url = reverse_lazy('profile:profile')  # Update to use the correct namespace

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user field to the current user
        form.instance.parent1 = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Generate the URL for the profile page of the current user
        return reverse_lazy('profile:profile', kwargs={'pk': self.request.user.pk})

class EditGymnastView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a Gymnast"""

    template_name = "gymnast/edit_gymnast.html"
    form_class = GymnastForm
    model = Gymnast

    def get_object(self, queryset=None):
        return get_object_or_404(Gymnast, pk=self.kwargs['pk'])

    def test_func(self):
        """Check if the current user matches the user associated with the gymnast being edited."""
        gymnast = self.get_object()
        return self.request.user == gymnast.user

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        return reverse_lazy('profile', kwargs={'pk': self.kwargs['pk']})
