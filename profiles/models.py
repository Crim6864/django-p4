from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """Profile Model"""

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    förnamn = models.CharField(max_length=20, blank=True)
    efternamn = models.CharField(max_length=20, blank=True)
    adress = models.CharField(max_length=55, blank=True)
    telefon = models.CharField(max_length=55, blank=True)
    # Add more fields as needed

    def __str__(self):
        return f"Profile for {self.user.username}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'profile'):
        Profile.objects.create(user=instance)

# Connect the signal handler function to the post_save signal of the User model
post_save.connect(create_user_profile, sender=User)