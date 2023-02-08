from django import forms
from .models import Post, Comment
# from image_uploader_widget.widgets import ImageUploaderWidget
from django.utils.translation import gettext_lazy as _



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'user', 'slug', 'status')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter caption'}),
            # 'image': forms.FileInput(attrs={'class': 'form-control'}),
            # 'image': ImageUploaderWidget(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ['content', 'parent']

        labels = {
            'content': _(''),
        }

        widgets = {
            'content': forms.TextInput(),
        }


# class PostForm(forms.ModelForm):
#     """Form for the image model"""
#     class Meta:
#         model = Post
#         fields = ('title', 'content', 'image', 'user', 'slug')
