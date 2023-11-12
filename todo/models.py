from django.db import models


class Todo(models.Model):
    """A model that contains todo data."""
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    is_completed = models.BooleanField(default=False)
    