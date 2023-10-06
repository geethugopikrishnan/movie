from django.db import models

# Create your models here.


class Movie(models.Model):
    objects = None
    name = models.CharField(max_length=300)
    desc = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='gallery')


def __str__(self):
    return self.name
