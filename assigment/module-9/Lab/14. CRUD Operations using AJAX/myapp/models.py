from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    experience = models.IntegerField()
    phone = models.CharField(max_length=15)