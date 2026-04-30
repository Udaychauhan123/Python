from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("update",update_data,name="update"),
    path("delete",delete_data,name="delete"),
]
