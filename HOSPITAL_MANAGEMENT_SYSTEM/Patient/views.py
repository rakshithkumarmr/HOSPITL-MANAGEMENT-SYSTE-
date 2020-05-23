from django.shortcuts import render, redirect
from django.contrib import messages
def Homepage(request):
    return render(request,"home.html")


def Aboutus(request):
    return render(request,"aboutus.html")


def Contact(request):
    return render(request,"contactus.html")


def contact_save(request):
    messages.success(request, "successfully querry asked, shortly we try to solve this")
    return redirect("contact")
