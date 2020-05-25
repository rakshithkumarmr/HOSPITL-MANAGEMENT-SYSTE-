from django import forms
import re
from HR.models import OutstandingModel

class OutstandingForm(forms.ModelForm):
    class Meta:
        model = OutstandingModel
        fields = "__all__"