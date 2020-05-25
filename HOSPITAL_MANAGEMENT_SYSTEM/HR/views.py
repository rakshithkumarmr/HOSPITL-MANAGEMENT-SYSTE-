from django.shortcuts import render, redirect
from django.contrib import messages
from Patient.models import PatientModel,UserModel
from doctor.models import DoctorModel
from HR.forms import OutstandingForm
from HR.models import OutstandingModel

def hr_page(request):
    res = request.session.get("username", None)
    if res:
        return render(request, 'hr/hr_mainpage.html')
    else:
        return redirect('login')

def hr_Aboutus(request):
    return render(request,"hr/hr_aboutus.html")


def hr_Contact(request):
    return render(request,"hr/hr_contactus.html")


def hr_contact_save(request):
    messages.success(request, "successfully querry asked, shortly we try to solve this")
    return redirect("hr_contact")

def hr_logout(request):
    try:
        del request.session['username']
        del request.session['user_id']
        return redirect('home')
    except KeyError:
        return redirect('home')

def hr_dashboard(request):
    try:
        data = DoctorModel.objects.all()
    except:
        data =[]
    try:
        dd1=DoctorModel.objects.filter(status="Active")
    except:
        dd1=[]
    td = len(data)
    dd =len(dd1)
    tp1 = PatientModel.objects.all()
    tp=len(tp1)
    return render(request,"hr/hr_dashboard.html",{"data":data,"td":td,"dd":dd,"tp":tp})

def del_doctor(request):
    id=request.GET.get("x")
    DoctorModel.objects.filter(id=id).delete()
    return redirect('hr_dashboard')


def update_doctor(request):
    id = request.POST.get("id")
    res = DoctorModel.objects.get(id=id)
    return render(request,"hr/update_doctor.html",{"data":res})


def d_update(request):
    id = request.POST.get("id")
    username = request.POST.get("username")
    un = UserModel.objects.get(username=username)
    name = request.POST.get("name")
    mobile = request.POST.get("mobile")
    email = request.POST.get("email")
    gender = request.POST.get("gender")
    age = request.POST.get("age")
    status = request.POST.get("status")
    dept = request.POST.get("dpt")
    attendence = request.POST.get("att")
    salary = request.POST.get("salary")
    DoctorModel(id=id,username=un,name=name,mobile=mobile,email=email,
                 gender=gender,age=age,status=status,department=dept,attendence=attendence,sallary=salary).save()
    return redirect('hr_dashboard')


def hr_accounting(request):
    data = OutstandingModel.objects.all()
    return render(request,"hr/hr_accounting.html",{"data":data})

def create_outstanding(request):
    if request.method == 'POST':
        ef = OutstandingForm(request.POST)
        if ef.is_valid():
            ef.save()
            messages.success(request,"successfully created")
            return redirect('hr_accounting')
        else:
            messages.success(request, ef.errors)
            return redirect('create_outstanding')
    return render(request,"hr/add_hr_outstanding.html",{"form":OutstandingForm()})