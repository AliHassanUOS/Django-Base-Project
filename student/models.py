from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Student(models.Model):

    stu_name = models.CharField(max_length=200)
    stu_roll = models.IntegerField()
    stu_email = models.EmailField(null= True)
    std_num = models.IntegerField(null=False, default=1)
    just_name = models.CharField(max_length=200,blank= True , name= False)
    status = models.BooleanField(blank=True ,null= False)


    
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.IntegerField()
    password = models.CharField(max_length=100)
    password1 = models.CharField(max_length=200)


class Person(models.Model):
    firstName = models.CharField(max_length = 100)
    middleName = models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100)
    phoneNumber = PhoneNumberField(unique = True, null = False, blank = False) # Here
    secondPhoneNumber = PhoneNumberField(null = True, blank = True) # Here