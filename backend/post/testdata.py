from datetime import datetime
from .models import Post
from user.models import CustomUser
from django.utils import timezone


def generate_post():
    for i in range(0, 50):
        Post.objects.all().delete()
        Post.objects.create(
            user=CustomUser.objects.first(),
            title=f"title {i}",
            slug=f"title-{i}",
            content=f"content of {i}",
            update=timezone.datetime.now(),
            created_at=timezone.datetime.now(),
        )
