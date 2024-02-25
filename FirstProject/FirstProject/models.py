from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 30)
    collegeID = models.IntegerField()
    age = models.IntegerField() 
class Profile(models.Model):
    email = models.CharField(max_length=50)
    pasw = models.CharField(max_length = 50)

