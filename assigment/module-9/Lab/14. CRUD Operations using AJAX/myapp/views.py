from django.shortcuts import render
from myapp.models import *
from django.http import JsonResponse,HttpResponse
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,"index.html")

def display(request):
    doctors = Doctor.objects.all()
    return JsonResponse({"doctors":list(doctors.values())})

def add_doctor(request):
    if request.method=='POST':
        data = request.POST
        
        name = data.get("name")
        specialization = data.get("specialization")
        experience = data.get("experience")
        phone = data.get("phone")

        Doctor.objects.create(name=name,specialization=specialization,experience=experience,phone=phone)

        return HttpResponse("Registration successfully !!!")
    

def delete_doctor(request):
    id  = request.GET['id']
    doctor = Doctor.objects.get(pk=id)
    doctor.delete()
    return HttpResponse("Doctor deleted !!!")


def edit_doctor(request):
    id  = request.GET['id']
    doctor = Doctor.objects.filter(id=id)
    return JsonResponse({"doctor":list(doctor.values())})


def update_doctor(request):
    if request.method=='POST':
        data = request.POST
        id = data.get("id")
        name = data.get("name")
        specialization = data.get("specialization")
        experience = data.get("experience")
        phone = data.get("phone")


        dr = Doctor.objects.get(pk=id)
        dr.name=name
        dr.specialization=specialization
        dr.experience=experience
        dr.phone=phone
        dr.save()

        return HttpResponse("Update successfully !!!")
    

def search(request):
    q = request.GET['q']

    # students = Student.objects.filter(name__startswith=q) or Student.objects.filter(email__startswith=q) or Student.objects.filter(age__startswith=q)

    doctor = Doctor.objects.filter(Q(name__startswith=q)|Q(specialization__startswith=q)|Q(experience__startswith=q)|Q(phone__startswith=q)) 

    return JsonResponse({"doctor":list(doctor.values())})