from django.db import models

# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=30)
    ### this class will be converted into database table

# def __str__(self):
#     return 'Employee Object with eno: +str(elf.no)'
