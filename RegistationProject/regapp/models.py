from django.db import models

# Create your models here.
class Employee(models.Model):
    EName=models.CharField(max_length=30)
    Enumber=models.IntegerField()
    EAddress=models.CharField(max_length=30)
    Esal=models.FloatField()