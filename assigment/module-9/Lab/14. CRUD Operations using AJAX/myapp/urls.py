from django.urls import path
from myapp.views import *

urlpatterns = [
    path("", index, name="index"),
    path("display", display, name="display"),
    path("adddoctor", add_doctor, name="adddoctor"),
    path("deletedoctor", delete_doctor, name="deletedoctor"),
    path("editdoctor", edit_doctor, name="editdoctor"),
    path("updatedoctor", update_doctor, name="updatedoctor"),
    path("search", search, name="search"),
]