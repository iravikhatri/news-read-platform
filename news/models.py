from django.db import models
from django.contrib.auth.models import User


class News(models.Model):

    title = models.CharField(max_length=256)
    content = models.TextField()
    image_url = models.URLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
