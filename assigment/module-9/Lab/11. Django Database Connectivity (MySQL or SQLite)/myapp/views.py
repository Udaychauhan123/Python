from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib import messages
# Create your views here.

def index(request):
    doctors = Doctor.objects.all()

    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        specialization = data.get("specialization")
        experience = data.get("experience")

        Doctor.objects.create(name=name,email=email,specialization=specialization,experience=experience)

        messages.success(request, "Doctor added successfully")
        return redirect("index")

    return render(request, "index.html", {'doctors': doctors})


#Delete

def delete(request):
    dele = request.GET['dele']
    dr = Doctor.objects.get(id=dele)
    dr.delete()
    return redirect("index")


#Update
def update(request):
    d = Doctor.objects.all()

    if request.method == "POST":
        data = request.POST
        id = data.get("id")
        name = data.get("name")
        email = data.get("email")
        specialization = data.get("specialization")
        experience = data.get("experience")

        dr = Doctor.objects.get(id=id)
        dr.name = name
        dr.email = email
        dr.specialization = specialization
        dr.experience = experience
        dr.save()

        return redirect('index')
    
    uid = request.GET['uid']
    dr = Doctor.objects.get(id=uid)
    return render(request, "index.html", {'doc': dr,'doctors': d,'message': 'data update'})