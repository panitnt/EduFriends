from re import sub
from time import time
from django.db import models

# Create your models here.
class Room(models.Model):
    subject = models.CharField(max_length=255)
    by = models.CharField(max_length=255)
    university = models.CharField(max_length=255, blank=True)
    date = models.DateField()
    time = models.TimeField()
    people = models.IntegerField()
    url = models.URLField()

    def __str__(self) -> str:
        return f'{self.subject} by {self.by} : {self.university} {self.date} {self.time}'