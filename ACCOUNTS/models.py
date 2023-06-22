from django.db import models
from django.contrib import auth


# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):
    
    def __str__(self):
        return "@{}".format(self.username)
    

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    specialization = models.CharField(max_length=50)

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_birth = models.DateField()
    gender = models.CharField(max_length=6)
    mobile = models.IntegerField()
    address = models.TextField()
    


class Patient_B(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_birth = models.DateField()
    gender = models.CharField(max_length=6)
    Health_Insurance_Card_number = models.IntegerField()
    mobile = models.IntegerField(null=True)
    address = models.TextField()

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
