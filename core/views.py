from django.shortcuts import render, redirect
from django.contrib.auth import logout


#create your views here
def main(request):
    return render(request, 'core/main.html',{})

def index(request):
    return render(request, 'core/index.html',{})

def base(request):
    return render(request, 'core/base.html',{})

def studios(request):
    return render(request, 'core/studios.html',{})

def apartments(request):
    return render(request, 'core/apartments.html',{})

def bedsitters(request):
    return render(request, 'core/bedsitters.html',{})


def dashboard(request):
    return render(request, 'authenticated/dashboard.html')

# class RegisterView(View):
def login(request):
    return render(request, "registration/login.html", {})

def password_reset_form(request):
    return render(request, "registration/password_reset_form.html", {})

def password_change_form(request):
    return render(request, "registration/password_change_form.html", {})


def logout_view(request):
    logout(request)
    return redirect(to='/')