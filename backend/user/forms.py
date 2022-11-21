from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreateForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", 'username', 'email', "image")


class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name",
                  'username', 'bio', 'email', "image")
