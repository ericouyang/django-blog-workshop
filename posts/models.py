from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    # timestamps
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
