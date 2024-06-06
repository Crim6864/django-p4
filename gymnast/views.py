from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin
from .models import Gymnast, GymnastGroup  # Import the Gymnast and GymnastGroup models
from .forms import GymnastForm, AssignGroupForm, MoveGymnastForm


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
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gymnasts'] = Gymnast.objects.all()  # Retrieve all gymnasts
        return context


class MoveGymnastView(LoginRequiredMixin, UserPassesTestMixin, UpdateView, FormMixin):
    model = Gymnast
    form_class = AssignGroupForm
    template_name = 'gymnast/move_gymnast.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['move_gymnast_form'] = MoveGymnastForm()
        context['gymnasts'] = Gymnast.objects.all()  # Retrieve all gymnasts
        return context

    def post(self, request, *args, **kwargs):
        selected_gymnasts_ids = request.POST.getlist('gymnasts')  # Get list of selected gymnast IDs from form data
        new_group_id = request.POST.get('grupp')  # Get the new group ID from form data
        new_group = GymnastGroup.objects.get(id=new_group_id)  # Retrieve the GymnastGroup instance
        for gymnast_id in selected_gymnasts_ids:
            gymnast = Gymnast.objects.get(id=gymnast_id)
            gymnast.grupp = new_group
            gymnast.save()
        return redirect(self.get_success_url())


class ViewGymnastView(LoginRequiredMixin, ListView):
    model = Gymnast
    template_name = 'gymnast/gymnast_list.html'
    context_object_name = 'gymnasts'

    def get_queryset(self):
        # Retrieve gymnasts belonging to either parent1 or parent2
        return Gymnast.objects.filter(Q(parent1=self.request.user) | Q(parent2=self.request.user))

def gymnasts_by_group_view(request):
    selected_group_id = request.GET.get('group')
    if selected_group_id:
        selected_group = get_object_or_404(GymnastGroup, id=selected_group_id)
        groups = GymnastGroup.objects.prefetch_related('gymnast_set').all()
        context = {
            'groups': groups,
            'selected_group': selected_group,
            'gymnasts': selected_group.gymnast_set.all(),
        }
    else:
        groups = GymnastGroup.objects.prefetch_related('gymnast_set').all()
        context = {
            'groups': groups,
            'selected_group': None,
            'gymnasts': Gymnast.objects.none(),
        }

    return render(request, 'gymnast/gymnasts_by_group.html', context)