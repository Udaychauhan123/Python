from django.urls import path
from myapp.views import *
urlpatterns = [
    path('', home, name='home'),
    path('profile',profile, name='profile'),
    path('contact',contact, name='contact'),
]
