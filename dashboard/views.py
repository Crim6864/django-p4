from django.views.generic import TemplateView

class UserDashboardView(TemplateView):
    template_name = 'user_dashboard.html'  # Change this to the appropriate template name

    # Optionally, you can override other methods such as get_context_data() if needed

class AdminDashboardView(TemplateView):
    template_name = 'admin_dashboard.html'  # Change this to the appropriate template name

    # Optionally, you can override other methods such as get_context_data() if needed
