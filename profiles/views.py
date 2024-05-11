from django.views.generic import TemplateView, CreateView, UpdateView
from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .models import Profile
from .forms import ProfileForm


class ProfileView(TemplateView):
    template_name = 'profiles/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile = None
        if hasattr(user, 'profile'):
            profile = user.profile
        context['profile'] = profile
        return context

class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a Profile"""

    template_name = "profiles/edit_profile.html"
    form_class = ProfileForm
    model = Profile

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user=self.request.user)

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        return super().form_valid(form)

    def test_func(self):
        """Check if the current user matches the user associated with the profile being edited."""
        profile = self.get_object()
        return self.request.user == profile.user

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})