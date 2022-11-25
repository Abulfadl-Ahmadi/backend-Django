from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


# class CustomUserCreateForm(UserCreationForm):

#     class Meta:
#         model = CustomUser
#         fields = ("first_name", "last_name", 'username', 'email', "image")

class CustomUserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username",
                  "email", "image", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name",
                  'username', 'bio', 'email', "image")


# from django.contrib.auth.models import User


# Create your forms here.
