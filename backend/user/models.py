from django.db import models
from django.contrib.auth.models import User, AbstractUser
from datetime import date
from PIL import Image
# from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager


__all__ = (
    'CustomUser',
)


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    # username = models.CharField(max_length=64, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='profile_pics',
                              default='profile_pics/default.png')
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width < 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    # @property
    # def age(self):
    #     today = date.today()
    #     age = today.year - self.birthdate.year - \
    #         ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
    #     return age
