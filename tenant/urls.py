from django.urls import path
from . import views

#create your views here

urlpatterns = [ 
    path('index/', views.index, name="index"),
]