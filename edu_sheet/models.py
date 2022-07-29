from django.db import models

# Create your models here.
class Sheet(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='edu_sheet/images/')
    contact = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name