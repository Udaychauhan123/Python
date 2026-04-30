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
        contact = data.get("contact")

        Doctor.objects.create(name=name,email=email,specialization=specialization,experience=experience,contact=contact)

        messages.success(request,"data inserted")

        return redirect(index)
    return render(request,"index.html",{'doctors': doctors})

def delete_data(request):
    did = request.GET['did']
    st = Doctor.objects.get(id=did)  
    st.delete()
    return redirect('index')    

def update_data(request):
    d = Doctor.objects.all()

    if request.method == "POST":
        data = request.POST
        id = data.get("id")
        name = data.get("name")
        email = data.get("email")
        specialization = data.get("specialization")
        experience = data.get("experience")
        contact = data.get("contact")

        st = Doctor.objects.get(id=id)
        st.name = name
        st.email = email
        st.specialization = specialization
        st.experience = experience
        st.contact = contact
        st.save()

        return redirect('index')   # fixed

    uid = request.GET.get('uid')   # safer
    st = Doctor.objects.get(id=uid)

    return render(request, "index.html", {
        'doctors': d,
        'doctor': st
    })
