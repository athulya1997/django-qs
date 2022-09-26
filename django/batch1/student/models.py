from django.db import models

# Create your models here.
class Reg(models.Model):
    fname=models.CharField(max_length=45)
    lname=models.CharField(max_length=45)
    age=models.IntegerField(default=0)
    place=models.CharField(max_length=45)

# foreign key
class UserLog(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    userid=models.ForeignKey(to=Reg,on_delete=models.CASCADE)

class Employee(models.Model):
    emp_name=models.CharField(max_length=45)
    emp_age=models.IntegerField()
    salary=models.FloatField()
    gender=models.CharField(max_length=45)

class UploadFile(models.Model):
    title=models.CharField(max_length=45)
    des=models.TextField()
    file=models.FileField(upload_to='uploads/files')

class UploadImage(models.Model):
    title=models.CharField(max_length=45)
    des=models.TextField()
    image=models.ImageField(upload_to='uploads/images')

class Register(models.Model):
    fname=models.CharField(max_length=45)
    lname=models.CharField(max_length=45)
    age=models.IntegerField()
    place=models.CharField(max_length=45)
    username=models.CharField(max_length=45)
    password=models.CharField(max_length=45)
