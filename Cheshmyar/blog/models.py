from django.db import models
from datetime import date

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    date = models.DateField()
    text = models.TextField()
    photo = models.ImageField(upload_to="photos/")

    def __str__(self):
        return self.title
