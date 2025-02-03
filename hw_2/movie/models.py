from django.db import models

# Create your models here.

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    producer = models.CharField(max_length=255)
    duration = models.IntegerField(help_text="Продолжительность фильма в секундах")

    def __str__(self):
        return self.title