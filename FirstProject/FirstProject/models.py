from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 30)
    collegeID = models.IntegerField()
    age = models.IntegerField() 
class Profile(models.Model):
    email = models.CharField(max_length=50)
    pasw = models.CharField(max_length = 50)

class Employee(models.Model):
    ename = models.CharField( max_length=50)
    esalary = models.FloatField(max_length = 50)
    eadd = models.CharField(max_length = 100)
    