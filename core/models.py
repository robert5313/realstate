from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Role(models.Model):
#     name = models.CharField(max_length=20)
#     description = models.TextField(default='')


PROPERTY_TYPE = (
    ('1', "Bedistters"),
    ('2', "Bedistters, 1 bedroom or more Apartments"),
    ('3', "Studio Apartments, bedsitters, 1 bedroom or more Apartments"),
)

class Property(models.Model):
    name= models.CharField(max_length=50, unique=True, blank=False,
                              error_messages={
                                  'unique': "A property with that name already exists.",
                              }) 
    address= models.TextField(max_length=100, default='')
    type = models.CharField(choices=PROPERTY_TYPE, max_length=50)
    floor = models.IntegerField() 
    county= models.CharField(max_length=50)
    city= models.CharField(max_length=50)
    capacity= models.IntegerField()
    description= models.TextField(max_length=100, default=True)
    account_number= models.IntegerField()
    rent_till_number= models.IntegerField()
    owner= models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

class Apartment(models.Model): 
    house_number = models.CharField(max_length=50)
    property_id = models.ForeignKey('Property',  on_delete=models.CASCADE ) # If a property is deleted, delete the apartment as well 
    occupant = models.ForeignKey('tenant.Tenant', on_delete=models.SET_NULL, null=True, blank=True)
    rent_price = models.IntegerField()
    features= models.TextField(max_length=100, default='')
    floor_number= models.IntegerField()
    rent_payment_status = models.BooleanField()

class Expense(models.Model):
    apartment_id = models.ForeignKey('Apartment', on_delete=models.CASCADE )
    amount = models.IntegerField()
    purpose = models.TextField(default='')
    date_incurred= models.DateTimeField(auto_now=True)

# Paid by tenants
class RentIncome(models.Model): 
    amount = models.IntegerField()
    date_received = models.DateTimeField(auto_now=True)
    apartment_id = models.ForeignKey('Apartment',  on_delete=models.CASCADE )
    user_id = models.ForeignKey('tenant.Tenant',  on_delete=models.CASCADE)