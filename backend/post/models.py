from django.db import models
from user.models import *
from PIL import Image
from django_cleanup import cleanup
from utils.utils import StatusOfPost
from user.models import *


class Post(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    content = models.TextField()
    image = models.FileField(blank=True, null=True, upload_to="photos")
    update = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=1, choices=StatusOfPost.choices, default=StatusOfPost.PUBLISH)

    def __str__(self) -> str:
        return f'{str(self.user)}:{self.title}'

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

    class Meta:
        ordering = ['created_at']


@cleanup.ignore
class MyModel(models.Model):
    image = models.FileField()


class Comment(models.Model):
    CommentPost = models.ForeignKey(Post , on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self' , null=True , blank=True , on_delete=models.CASCADE , related_name='replies')

    class Meta:
        ordering=['-date_posted']

    def __str__(self):
        return str(self.author) + ' comment ' + str(self.content)

    @property
    def children(self):
        return Comment.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False
    