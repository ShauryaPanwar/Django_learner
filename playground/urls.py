# Map urls with view fuctions
from django.urls import path
from . import  views


# URLConfing
urlpatterns =[
    path('hell/',views.say_hello)
]