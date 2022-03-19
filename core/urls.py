from django.urls import path
from django.contrib.auth import views
from . import views

#create your views here

urlpatterns = [
    path('', views.main, name="main"),
    path('index/', views.index, name="index"),
    path('logout', views.logout_view, name="logout"),
    path('studios',  views.studios, name="studios"),
    path('apartments',  views.apartments, name="apartments"),
    path('bedsitters',  views.bedsitters, name="bedsitters")


]