from django.shortcuts import render, redirect
from django.contrib import messages
from Patient.forms import UserRegisterForm,PatientRegisterForm
from Patient.models import UserModel,PatientModel
from Receptionist.models import AppointmentsModel
from HR.models import OutstandingModel
from doctor.models import Prescription

def Homepage(request):
    return render(request,"home.html")


def Aboutus(request):
    return render(request,"aboutus.html")


def Contact(request):
    return render(request,"contactus.html")


def contact_save(request):
    messages.success(request, "successfully querry asked, shortly we try to solve this")
    return redirect("contact")

def register(request):
    gef=UserRegisterForm()
    if request.method == 'POST':
        ef = UserRegisterForm(request.POST)
        if ef.is_valid():
            fname = request.POST.get("firstname")
            lname = request.POST.get("lastname")
            uname = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            confirm_password = request.POST.get("rpass")
            type =request.POST.get("usertype")
            if password == confirm_password:
                if UserModel.objects.filter(username=uname).exists():
                    messages.success(request,"Username Exists")
                    return render(request, "register.html",{"form":ef})
                elif UserModel.objects.filter(email=email).exists():
                    messages.success(request, "Email-Id  Exists")
                    return render(request, "register.html",{"form":ef})
                else:
                    UserModel(firstname=fname,lastname=lname,username=uname,email=email,password=password,usertype=type).save()
                    messages.success(request, "Successfully Registered")
                    return redirect("login")
            else:
                messages.success(request, "Password Not Matching")
                return render(request, "register.html",{"form":ef})
        else:
            messages.success(request,ef.errors)
            return render(request, "register.html", {"form": ef})
    else:
        return render(request,"register.html",{"form":gef})


def login(request):
    return render(request, "login.html")

def login_check(request):
    uname=request.POST.get("username")
    upass=request.POST.get("password")
    if uname == "ramu" and upass =="12345678":
        request.session['username'] = uname
        request.session['user_id'] = "receptionist"
        return redirect('receptionist_page')
    elif uname == "rak" and upass =="12345678":
        request.session['username'] = uname
        request.session['user_id'] = "hr"
        return redirect('hr_page')
    else:
        try:
            sam = UserModel.objects.get(username=uname,password=upass)
            request.session['username'] = sam.username
            request.session['user_id'] = sam.id
            if sam.usertype == "Doctor":
                return redirect('doctor_page')
            else:
                return redirect('patient_page')
        except:
            messages.success(request,"Invalid User")
            return render(request, 'login.html' )

def patient_page(request):
    res = request.session.get("username", None)
    if res:
        return render(request, 'patient/patient_mainpage.html')
    else:
        return redirect('login')

def patient_Aboutus(request):
    return render(request,"patient/patient_aboutus.html")


def patient_Contact(request):
    return render(request,"patient/patient_contactus.html")


def patient_contact_save(request):
    messages.success(request, "successfully querry asked, shortly we try to solve this")
    return redirect("patient_contact")

def patient_logout(request):
    try:
        del request.session['username']
        del request.session['user_id']
        return redirect('home')
    except KeyError:
        return redirect('home')


def patient_appoint(request):
    try:
        user_id = request.session.get("user_id", None)
        p_id =PatientModel.objects.get(username_id=user_id).id
        res =AppointmentsModel.objects.filter(patient_id=p_id)
        return render(request,"patient/patient_appoint.html",{"data":res})
    except:
        return render(request,"patient/patient_appoint.html",{"data":[]})

def patient_invoice_payment(request):
    try:
        user_id = request.session.get("user_id", None)
        p_id = PatientModel.objects.get(username_id=user_id).id
        res = OutstandingModel.objects.filter(patient_name_id=p_id)
        return render(request,"patient/patient_invoice_payment.html",{"data":res})
    except:
        return render(request,"patient/patient_invoice_payment.html",{"data":{}})

def patient_medical_history(request):
    try:
        user_id = request.session.get("user_id", None)
        p_id = PatientModel.objects.get(username_id=user_id).id
        res = Prescription.objects.filter(patient_id=p_id)
        return render(request,"patient/patient_medical_historyt.html",{"data":res})
    except:
        return render(request,"patient/patient_medical_historyt.html",{"data":[]})

def patient_profile(request):
    gef = PatientRegisterForm()
    if request.method == 'POST':
        ef = PatientRegisterForm(request.POST)
        if ef.is_valid():
            username = request.POST.get("username")
            un =UserModel.objects.get(username=username)
            name = request.POST.get("name")
            mobile = request.POST.get("mobile")
            email = request.POST.get("email")
            gender = request.POST.get("gender")
            age = request.POST.get("age")
            address = request.POST.get("address")
            blood_group = request.POST.get("blood_group")
            PatientModel(username=un,name=name,mobile=mobile,email=email,gender=gender,age=age,address=address,blood_group=blood_group).save()
            messages.success(request, "Successfully Registered")
            return render(request, "patient/patient_profile.html",{"form": gef})
        else:
            messages.success(request, ef.errors)
            return render(request, "patient/patient_profile.html", {"form": ef})
    else:
        return render(request, "patient/patient_profile.html", {"form": gef})

