from django import forms
import re
from Receptionist.models import AppointmentsModel

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = AppointmentsModel
        fields = "__all__"