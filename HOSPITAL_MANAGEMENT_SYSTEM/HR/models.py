from django.db import models

from Patient.models import PatientModel


class OutstandingModel(models.Model):
    date =models.DateField(auto_now_add=True)
    patient_name =models.ForeignKey(PatientModel,on_delete=models.CASCADE)
    paid = models.DecimalField(max_digits=10,decimal_places=2)
    outstanding = models.DecimalField(max_digits=10,decimal_places=2)
