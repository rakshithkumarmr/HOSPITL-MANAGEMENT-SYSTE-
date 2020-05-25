from django import forms
import re
from doctor.models import Prescription

class DoctorRegisterForm(forms.Form):
    def clean_name(self):
        fn=self.cleaned_data["name"]
        res = re.match("^[A-Za-z ]*$",fn)
        if res:
            return fn
        else:
            raise forms.ValidationError("Invalid name")
    def clean_mobile(self):
        pno=self.cleaned_data['mobile']
        pn=re.findall(r'(^[6-9]\d{9}$)',str(pno))
        if pn:
            return pno
        else:
            raise forms.ValidationError("Invalid Mobile No")
    gen = (('MALE', 'Male'), ('FEMALE', 'Female'))
    st = (('Active', 'Active'), ('Inactive', 'Inactive'))
    dpt = (('OPD', 'OPD'),('Oncology', 'Oncology'),('Neurology','Neurology'))
    username = forms.CharField(label="Username", max_length=20)
    name = forms.CharField(label="Name",max_length=30)
    mobile = forms.IntegerField(label="Mobile No")
    email = forms.EmailField(label="Email")
    gender = forms.ChoiceField(choices=gen)
    age = forms.IntegerField(min_value=1,max_value=120)
    status =forms.ChoiceField(choices=st)
    department =forms.ChoiceField(choices=dpt)
    attendence = forms.IntegerField(required=False)
    salary = forms.DecimalField(max_digits=12,decimal_places=2,required=False)

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = "__all__"