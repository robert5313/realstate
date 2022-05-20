from tkinter.simpledialog import askfloat
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import CustomerRequestForm
from core.models import Apartment, CustomerRequest
from tenant.models import Tenant

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
    apartments = Apartment.objects.all().order_by('id')
    context = {'apartments': apartments}
    return render(request, 'core/apartments.html', context)

def apartment(request, house_number):
    apartment = Apartment.objects.get(house_number=house_number)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CustomerRequestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data)
            cust_req = CustomerRequest(
                phone_number = form.cleaned_data["phone_number"],
                email = form.cleaned_data["email"],
                request = form.cleaned_data["request"],
                first_name = form.cleaned_data["first_name"],
                last_name = form.cleaned_data["last_name"],
                approval_status = False,
                # user = user
                apartment = apartment
            )
            cust_req.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/dashboard/')

    form = CustomerRequestForm()
    context = {'apartment': apartment, 'house_number': house_number, "form": form}

    return render(request, 'core/apartment.html', context)

def bedsitters(request):
    return render(request, 'core/bedsitters.html',{})

def dashboard(request):
    user_id = request.user.id
    tenant = Tenant.objects.get(user_id=user_id)
    apartment = Apartment.objects.get(occupant_id=tenant.id)
    context = { 'user_id': user_id, 'tenant': tenant, 'apartment': apartment}
    return render(request, 'authenticated/dashboard.html', context)

def login(request):
    return render(request, "registration/login.html", {})

def password_reset_form(request):
    return render(request, "registration/password_reset_form.html", {})

def password_change_form(request):
    return render(request, "registration/password_change_form.html", {})

def logout_view(request):
    logout(request)
    return redirect(to='/')