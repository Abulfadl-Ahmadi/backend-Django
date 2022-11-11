from django.db import models
from django.contrib.auth.models import User
from datetime import date
from PIL import Image


# __all__ = (
#     'Profile',
#     )


# class User(models.Model):
#     username = models.ForeignKey(User, on_delete=models.CASCADE)
#     profile_image = models.ImageField(blank=True, null=True)
#     bio = models.CharField(max_length=255, blank=True, null=True)
#     birthdate = models.DateField(blank=True, null=True)
#     email = models.EmailField(unique=True, blank=True, null=True)
#     update = models.DateTimeField(auto_now=True)
#     created_at = models.DateTimeField(auto_now_add=True)


#     @property
#     def age(self):
#         today = date.today()
#         age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
#         return age


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(
        upload_to='profile_pics', null=True, blank=True)
    birthdate = models.DateField(blank=True, null=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width < 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birthdate.year - \
            ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age
