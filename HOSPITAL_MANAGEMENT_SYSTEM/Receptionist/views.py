from django.shortcuts import render, redirect
from django.contrib import messages
from Receptionist.models import AppointmentsModel
from Patient.models import PatientModel,UserModel
from Receptionist.forms import AppointmentForm

def receptionist_page(request):
    res = request.session.get("username", None)
    if res:
        return render(request, 'receptionist/receptionist_mainpage.html')
    else:
        return redirect('login')

def receptionist_Aboutus(request):
    return render(request,"receptionist/receptionist_aboutus.html")


def receptionist_Contact(request):
    return render(request,"receptionist/receptionist_contactus.html")


def receptionist_contact_save(request):
    messages.success(request, "successfully querry asked, shortly we try to solve this")
    return redirect("receptionist_contact")

def receptionist_logout(request):
    try:
        del request.session['username']
        del request.session['user_id']
        return redirect('home')
    except KeyError:
        return redirect('home')


def receptionist_dashboard(request):
    try:
        data = AppointmentsModel.objects.all()
    except:
        data =[]
    try:
        nc=AppointmentsModel.objects.filter(status="Completed")
    except:
        nc=[]
    ta = len(data)
    ad =len(nc)
    ua =ta-ad
    data1 = PatientModel.objects.all()
    return render(request,"Receptionist/receptionist_dashboard.html",{"data":data,"ta":ta,"ad":ad,"ua":ua,"data1":data1})


def create_appointment(request):
    if request.method == 'POST':
        ef = AppointmentForm(request.POST)
        if ef.is_valid():
            ef.save()
            messages.success(request,"successfully created")
            return redirect('receptionist_dashboard')
        else:
            messages.success(request, ef.errors)
            return redirect('create_appointment')
    return render(request,"Receptionist/add_receptionist_appointments.html",{"form":AppointmentForm()})


def del_pt(request):
    id=request.GET.get("x")
    PatientModel.objects.filter(id=id).delete()
    return redirect('receptionist_dashboard')


def update_pt(request):
    id = request.POST.get("id")
    res = PatientModel.objects.get(id=id)
    return render(request,"Receptionist/update_pt.html",{"data":res})


def p_update(request):
    id = request.POST.get("id")
    username = request.POST.get("username")
    un = UserModel.objects.get(username=username)
    name = request.POST.get("name")
    mobile = request.POST.get("mobile")
    email = request.POST.get("email")
    gender = request.POST.get("gender")
    age = request.POST.get("age")
    address = request.POST.get("address")
    blood = request.POST.get("blood")
    PatientModel(id=id,username=un,name=name,mobile=mobile,email=email,
                 gender=gender,age=age,address=address,blood_group=blood).save()
    return redirect('receptionist_dashboard')