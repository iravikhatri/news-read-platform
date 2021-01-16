from django.db import models


class News(models.Model):

    title = models.CharField(max_length=256)
    content = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.title
