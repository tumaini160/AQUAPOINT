from django.db import models

# Create your models here.
from django.db import models

class Table1(models.Model): 
    Name = models.CharField(max_length=10000) 
    Number = models.PositiveIntegerField()
    Coordinates = models.CharField(max_length=1000000)
    Date = models.DateTimeField(auto_now_add=True)

class Table2(models.Model):  
    Coordinates = models.CharField(max_length=1000000)
    SensorValue = models.PositiveIntegerField()
    Date = models.DateTimeField(auto_now_add=True)