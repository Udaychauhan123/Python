from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name