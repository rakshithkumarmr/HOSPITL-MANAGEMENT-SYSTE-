from django.db import models
from Patient.models import UserModel,PatientModel

class DoctorModel(models.Model):
    name = models.CharField(max_length=30)
    mobile =models.IntegerField()
    email = models.EmailField()
    gender =models.CharField(max_length=6)
    age =models.IntegerField()
    status =models.CharField(max_length=10)
    department =models.CharField(max_length=25)
    attendence = models.IntegerField(default=0)
    sallary = models.DecimalField(max_digits=12,decimal_places=2,default=0)
    username =models.ForeignKey(UserModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Prescription(models.Model):
    prescription = models.CharField(max_length=100)
    disease = models.CharField(max_length=30)
    patient = models.ForeignKey(PatientModel,on_delete=models.CASCADE)
