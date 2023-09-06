from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class RandomStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)