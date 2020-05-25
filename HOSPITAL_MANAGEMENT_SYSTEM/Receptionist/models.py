from django.db import models
from Patient.models import PatientModel
from doctor.models import DoctorModel

class AppointmentsModel(models.Model):
    st =(('Pending','Pending'),('Completed','Completed'))
    date = models.DateField()
    time = models.TimeField()
    doctor = models.ForeignKey(DoctorModel,on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientModel,on_delete=models.CASCADE)
    status = models.CharField(max_length=10,choices=st)

