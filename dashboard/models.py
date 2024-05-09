from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """Profile Model"""

    user = models.ForeignKey(User, related_name="profile", on_delete=models.CASCADE)
    förnamn = models.CharField(max_length=20, blank=False)
    efternamn = models.CharField(max_length=20, blank=False)
    adress = models.CharField(max_length=55, blank=False)
    telefon = models.IntegerField(blank=False)
    # Add more fields as needed

    def __str__(self):
        return f"Profile for {self.user.username}"


class Gymnast(models.Model):
    """Gymnast Model"""

    user = models.ForeignKey(
        User, related_name="gymnast_profile", on_delete=models.CASCADE
    )
    förnamn = models.CharField(max_length=20, blank=False)
    efternamn = models.CharField(max_length=20, blank=False)
    personnummer = models.IntegerField(blank=False)
    grupp = models.CharField(max_length=20, blank=True)
    # Add more fields as needed

    def __str__(self):
        return f"Gymnast profile for {self.user.username}"


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
