"""HOSPITAL_MANAGEMENT_SYSTEM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Patient import views as p_views
from doctor import views as d_views
from Receptionist import views as r_views
from HR import views as hr_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',p_views.Homepage,name="home"),
    path('aboutus/',p_views.Aboutus,name="aboutus"),
    path('contact/',p_views.Contact,name="contact"),
    path('contact_save/',p_views.contact_save,name="contact_save"),
    path('register/',p_views.register,name="register"),
    path('login',p_views.login,name="login"),
    path('login_check/',p_views.login_check,name="login_check"),

    path('patient_page/',p_views.patient_page,name="patient_page"),
    path('patient_aboutus/',p_views.patient_Aboutus,name="patient_aboutus"),
    path('patient_contact/',p_views.patient_Contact,name="patient_contact"),
    path('patient_contact_save/',p_views.patient_contact_save,name="patient_contact_save"),
    path('patient_appoint/',p_views.patient_appoint,name="patient_appoint"),
    path('patient_invoice_payment/',p_views.patient_invoice_payment,name="patient_invoice_payment"),
    path('patient_medical_history/',p_views.patient_medical_history,name="patient_medical_history"),
    path('patient_profile/',p_views.patient_profile,name="patient_profile"),
    path('patient_logout/',p_views.patient_logout,name="patient_logout"),

    path('doctor_page/',d_views.doctor_page,name="doctor_page"),
    path('doctor_aboutus/',d_views.doctor_Aboutus,name="doctor_aboutus"),
    path('doctor_contact/',d_views.doctor_Contact,name="doctor_contact"),
    path('doctort_contact_save/',d_views.doctor_contact_save,name="doctor_contact_save"),
    path('doctor_appoint/',d_views.doctor_appoint,name="doctor_appoint"),
    path('doctor_prescription/',d_views.doctor_prescription,name="doctor_prescription"),
    path('add_doctor_prescription/',d_views.add_doctor_prescription,name="add_doctor_prescription"),
    path('doctor_profile/',d_views.doctor_profile,name="doctor_profile"),
    path('doctor_logout/',d_views.doctor_logout,name="doctor_logout"),

    path('receptionist_page/',r_views.receptionist_page,name="receptionist_page"),
    path('receptionist_aboutus/',r_views.receptionist_Aboutus,name="receptionist_aboutus"),
    path('receptionist_contact/',r_views.receptionist_Contact,name="receptionist_contact"),
    path('receptionist_contact_save/',r_views.receptionist_contact_save,name="receptionist_contact_save"),
    path('receptionist_dashboard/',r_views.receptionist_dashboard,name="receptionist_dashboard"),
    path('create_appointment/',r_views.create_appointment,name="create_appointment"),
    path('del_pt/',r_views.del_pt,name="del_pt"),
    path('update_pt/',r_views.update_pt,name="update_pt"),
    path('p_update/',r_views.p_update,name="p_update"),
    path('receptionist_logout/',r_views.receptionist_logout,name="receptionist_logout"),

    path('hr_page/', hr_views.hr_page, name="hr_page"),
    path('hr_aboutus/', hr_views.hr_Aboutus, name="hr_aboutus"),
    path('hr_contact/', hr_views.hr_Contact, name="hr_contact"),
    path('hr_contact_save/', hr_views.hr_contact_save, name="hr_contact_save"),
    path('hr_dashboard/',hr_views.hr_dashboard,name="hr_dashboard"),
    path('del_doctor/',hr_views.del_doctor,name="del_doctor"),
    path('update_doctor/',hr_views.update_doctor,name="update_doctor"),
    path('d_update/',hr_views.d_update,name="d_update"),
    path('hr_accounting/',hr_views.hr_accounting,name="hr_accounting"),
    path('create_outstanding/',hr_views.create_outstanding,name="create_outstanding"),
    path('hr_logout/',hr_views.hr_logout,name="hr_logout"),
]
