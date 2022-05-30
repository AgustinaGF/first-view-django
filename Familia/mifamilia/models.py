from django.db import models

# Create your models here.
class Family (models.Model):
    nombre=models.CharField(max_length=30)
    edad=models.CharField(max_length=3)
    nacimiento=models.DateField()
