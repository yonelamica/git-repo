import datetime
from django.db import models
from django.utils import timezone

# ceated a class called Poll
class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    release_date = models.DateField()

    
# created a class called policy
class Policy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


