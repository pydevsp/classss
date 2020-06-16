from django.db import models


# Create your models here.
class Movie(models.Model):
    Rdate = models.DateField()
    MovieName = models.CharField(max_length=20)
    Rating = models.IntegerField()
    