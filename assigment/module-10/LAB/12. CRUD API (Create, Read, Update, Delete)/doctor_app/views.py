from django.shortcuts import render
from doctor_app.models import *
from doctor_app.serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class doctordata(APIView):
    def get(self,request):
        doctor = Doctor.objects.all()
        ser = DoctorSerializer(doctor,many = True)
        return Response({"data":ser.data})
    
    def post(self,request):
        ser = DoctorSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"data":ser.data,"message":"data insrted"})
        else:
            return Response({"errors":ser.errors,"message":"Something went Wrnog"})
        
class doctorupdate(APIView):
    def put(self,request,id):
        doctor = Doctor.objects.get(id=id)
        ser = DoctorSerializer(doctor,request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response({"data":ser.data,"message":"data successfully update"})
        else:
            return Response({"errors":ser.errors,"message":"Somthing went wrong in update"})
        
    def delete(self,request,id):
        doctor = Doctor.objects.get(id=id)
        doctor.delete()
        return Response({"message":"data successfully deleted"})

