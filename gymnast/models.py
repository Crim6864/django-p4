from django.db import models
from django.contrib.auth.models import User

class GymnastGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Gymnast(models.Model):
    """Gymnast Model"""

    user = models.ForeignKey(User, related_name="gymnast_profile", on_delete=models.CASCADE)
    förnamn = models.CharField(max_length=20, blank=True)
    efternamn = models.CharField(max_length=20, blank=True)
    personnummer = models.CharField(max_length=55, blank=True)
    grupp = models.ForeignKey(GymnastGroup, on_delete=models.SET_NULL, null=True, blank=True)
    parent1 = models.ForeignKey(User, related_name="parent1_gymnasts", on_delete=models.CASCADE, null=True, blank=True)
    parent2 = models.ForeignKey(User, related_name="parent2_gymnasts", on_delete=models.CASCADE, null=True, blank=True)
    # Add more fields as needed

    def __str__(self):
        return f"Gymnast profile for {self.user.username}"
