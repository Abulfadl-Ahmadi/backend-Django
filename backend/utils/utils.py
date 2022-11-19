from django.db import models


class StatusOfPost(models.TextChoices):
    DRAFT = "D", "Draft"
    PUBLISH = "P", "Publish"
