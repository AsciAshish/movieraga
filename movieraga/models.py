from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    name = models.CharField(max_length=256)
    poster_url = models.CharField(max_length=1024)
    video_url = models.CharField(max_length=1024)

    def __str__(self):
        return self.name
