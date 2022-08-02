from django.db import models

# Create your models here.
class Tutor(models.Model):
    nickname = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    age = models.IntegerField()
    subject = models.CharField(max_length=500)
    education = models.TextField(blank=False)
    picture = models.ImageField(upload_to='tutors/images/')
    contact = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.fullname} ({self.nickname})'