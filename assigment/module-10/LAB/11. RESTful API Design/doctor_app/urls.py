from django.urls import path
from doctor_app.views import *

urlpatterns = [
    path("doctor",doctordata.as_view()),
    path("doctor/<id>",doctorupdate.as_view())
]
