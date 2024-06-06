# gymnast/apps.py
from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.db.utils import OperationalError, ProgrammingError

class GymnastConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "gymnast"

    def create_groups(self, sender, **kwargs):
        # Import the Group model here to avoid circular import
        from .models import GymnastGroup

        # List of groups to be created
        group_names = [
            "Lille Skutt", "Bamse", "Brummelisa", "Lejonen", "Delfinerna", 
            "Fiskarna", "Parkour", "Grodorna", "Bävrarna"
        ]
        try:
            for group_name in group_names:
                GymnastGroup.objects.get_or_create(name=group_name)
        except (OperationalError, ProgrammingError):
            # This is expected during initial migrations, so we can ignore it
            pass

    def ready(self):
        # Connect the create_groups function to the post_migrate signal
        post_migrate.connect(self.create_groups, sender=self)
