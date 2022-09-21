from django.db import models
from django.contrib.auth.models import User
from datetime import date


class User(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    update = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    @property
    def age(self):
        today = date.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age