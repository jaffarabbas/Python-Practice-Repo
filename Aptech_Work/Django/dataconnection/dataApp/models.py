from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=12)
    message = models.TextField(max)
    date = models.DateField()

    def __str__(self):
        return self.name
