from django.db import models

# Create your models here.

class HDBResaleFlat(models.Model):
    month = models.CharField(max_length=10)
    town = models.CharField(max_length=150)
    # flatType = models.CharField(max_length=150)
    # block = models.CharField(max_length=150)
    # streetName = models.CharField(max_length=150)
    # storeyRange = models.CharField(max_length=150)
    # floorAreaSqm = models.CharField(max_length=150)
    # flatModel = models.CharField(max_length=150)
    # leaseCommenceDate = models.CharField(max_length=150)
    # remainingLease = models.CharField(max_length=150)
    # resalePrice = models.CharField(max_length=150)
    #
    # def __str__(self):
    #     return self.streetName