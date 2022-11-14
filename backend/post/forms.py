from django import forms
from .models import Post
from image_uploader_widget.widgets import ImageUploaderWidget


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title', 'content', 'image', 'user', 'slug')

#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
#             'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter caption'}),
#             # 'image': forms.FileInput(attrs={'class': 'form-control'}),
#             'image': ImageUploaderWidget(attrs={'class': 'form-control', 'name': 'image'}),
#             'user': forms.Select(attrs={'class': 'form-control'}),
#         }


class PostForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'user', 'slug')
