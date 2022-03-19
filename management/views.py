from django.shortcuts import render

#create your views
def dashboard(request):
    return render(request, 'home.html',{})