from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Optionally extend the User model (e.g., add profile picture or additional fields)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username
