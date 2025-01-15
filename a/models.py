from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    usertype=models.CharField(max_length=20)

class Teacher(models.Model):
    fteacher=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=20, unique=True, null=False)
    email=models.EmailField(unique=True)
    phoneno=models.IntegerField(null=False, unique=True)
    gender=models.CharField(max_length=10, null=False)
    department=models.CharField(max_length=30, null=False)
    age=models.IntegerField()
    username=models.CharField(max_length=20, null=False, unique=True)
    password=models.CharField(max_length=50, null=False, unique=True)


class Student_not_approved(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    phoneno=models.IntegerField(null=False, unique=True)
    gender=models.CharField(max_length=10)
    department=models.CharField(max_length=30)
    age=models.IntegerField()
    username=models.CharField(max_length=20, null=False, unique=True)
    password=models.CharField(max_length=50, unique=True)

class Student_approved(models.Model):
    fkstud1=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    phoneno=models.IntegerField(null=False, unique=True)
    gender=models.CharField(max_length=10)
    department=models.CharField(max_length=30)
    age=models.IntegerField()
    username=models.CharField(max_length=20, null=False, unique=True)
    password=models.CharField(max_length=50, null=False, unique=True)