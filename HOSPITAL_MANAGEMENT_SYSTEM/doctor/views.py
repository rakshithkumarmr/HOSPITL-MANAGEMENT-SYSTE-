from django.shortcuts import render,redirect
from django.contrib import messages
from doctor.forms import DoctorRegisterForm,PrescriptionForm
from Patient.models import UserModel,PatientModel
from doctor.models import DoctorModel,Prescription
from Receptionist.models import AppointmentsModel

def doctor_page(request):
    res = request.session.get("username", None)
    if res:
        return render(request, 'doctor/doctor_mainpage.html')
    else:
        return redirect('login')

def doctor_Aboutus(request):
    return render(request,"doctor/doctor_aboutus.html")


def doctor_Contact(request):
    return render(request,"doctor/doctor_contactus.html")


def doctor_contact_save(request):
    messages.success(request, "successfully querry asked, shortly we try to solve this")
    return redirect("doctor_contact")

def doctor_logout(request):
    try:
        del request.session['username']
        del request.session['user_id']
        return redirect('home')
    except KeyError:
        return redirect('home')

def doctor_profile(request):
    gef = DoctorRegisterForm()
    if request.method == 'POST':
        ef = DoctorRegisterForm(request.POST)
        if ef.is_valid():
            username = request.POST.get("username")
            un =UserModel.objects.get(username=username)
            name = request.POST.get("name")
            mobile = request.POST.get("mobile")
            email = request.POST.get("email")
            gender = request.POST.get("gender")
            age = request.POST.get("age")
            status = request.POST.get("status")
            department = request.POST.get("department")
            attendence = 0
            salary = 0
            DoctorModel(username=un,name=name,mobile=mobile,email=email,gender=gender,age=age,status=status,
                        department=department,attendence=attendence,sallary=salary).save()
            messages.success(request, "Successfully Registered")
            return render(request, "doctor/doctor_profile.html",{"form": gef})
        else:
            messages.success(request, ef.errors)
            return render(request, "doctor/doctor_profile.html", {"form": ef})
    else:
        return render(request, "doctor/doctor_profile.html", {"form": gef})

def doctor_appoint(request):
    try:
        user_id = request.session.get("user_id", None)
        d_id = DoctorModel.objects.get(username_id=user_id).id
        res = AppointmentsModel.objects.filter(doctor_id=d_id)
        return render(request,"doctor/doctor_appoint.html",{"data":res})
    except:
        return render(request,"doctor/doctor_appoint.html",{"data":[]})

def doctor_prescription(request):
    try:
        data = Prescription.objects.all()
        return render(request,"doctor/doctor_prescription.html",{"data":data})
    except:
        return render(request,"doctor/doctor_prescription.html",{"data":[]})


def add_doctor_prescription(request):
    if request.method == 'POST':
        ef = PrescriptionForm(request.POST)
        if ef.is_valid():
            ef.save()
            messages.success(request,"successfully created")
            return redirect('doctor_prescription')
        else:
            messages.success(request, ef.errors)
            return redirect('add_doctor_prescription')
    return render(request,"add_doctor_prescription.html",{"form":PrescriptionForm()})