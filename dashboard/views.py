from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from .models import Profile, Gymnast
from .forms import ProfileForm


class Profile(TemplateView):
    template_name = 'dashboard/profile.html'

def get_context_data(self, **kwargs):
    profile = Profile.objects.get(user=self.kwargs["pk"])
    context = {
        'profile' : profile
    }

    return context


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a Profile"""

    form_class = ProfileForm
    model = Profile

    def form_valid(self, form):
        self.success_url = f'/profile/view/{self.kwargs["pk"]}'
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user