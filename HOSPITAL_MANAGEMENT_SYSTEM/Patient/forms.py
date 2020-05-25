from django import forms
import re

class UserRegisterForm(forms.Form):
    def clean_firstname(self):
        fn=self.cleaned_data["firstname"]
        res = re.match("^[A-Za-z ]*$",fn)
        if res:
            return fn
        else:
            raise forms.ValidationError("Invalid firstname")
    def clean_lastname(self):
        ln=self.cleaned_data["lastname"]
        res = re.match("^[A-Za-z ]*$",ln)
        if res:
            return ln
        raise forms.ValidationError("Invalid Lastname")
    cho =(('Patient','Patient'),('Doctor','Doctor'))
    firstname = forms.CharField(label="First Name",max_length=20)
    lastname = forms.CharField(label="Last Name", max_length=20)
    username = forms.CharField(label="Username", max_length=20)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput,min_length=8)
    rpass = forms.CharField(label="Re-Enter Password", widget=forms.PasswordInput, min_length=8)
    usertype = forms.ChoiceField(choices=cho)

class PatientRegisterForm(forms.Form):
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
    bg = (('A+', 'A+'), ('A-', 'A-'),('A+', 'A+'),('B+', 'B+'),('B-', 'B-'),('O+', 'O+'),('O-', 'O-'),('AB+', 'AB-'))
    username = forms.CharField(label="Username", max_length=20)
    name = forms.CharField(label="Name",max_length=30)
    mobile = forms.IntegerField(label="Mobile No")
    email = forms.EmailField(label="Email")
    gender = forms.ChoiceField(choices=gen)
    age = forms.IntegerField(min_value=1,max_value=120)
    address =forms.CharField(max_length=100)
    blood_group =forms.ChoiceField(choices=bg)
