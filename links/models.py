from django.db import models
from django.utils import timezone

class Link(models.Model):
    original_url = models.URLField()
    shortened_url = models.CharField(max_length=6, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

