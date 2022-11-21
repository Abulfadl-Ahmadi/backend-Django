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

    def create_user(self, username, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **extra_fields):
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
        return self.create_user(username, email, password, **extra_fields)


# class Follow(models.Model):
#     follower = models.ForeignKey(
#         "CustomUser", on_delete=models.CASCADE, related_name="follower")
#     following = models.ForeignKey(
#         "CustomUser", on_delete=models.CASCADE, related_name="following")
#     created = models.DateTimeField(auto_now_add=True)


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True,  null=True)
    bio = models.TextField(blank=True,  null=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='profile_pics',
                              default='profile_pics/default.png')
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username}"

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width < 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    # @property
    # def get_followers(self):
    #     '''
    #     set a query to search followings of self.user
    #     '''
    #     followers = Follow.objects.filter(follower=self.user)

    # @property
    # def get_following(self):
    #     followings = Follow.objects.filter(following=self.user)
