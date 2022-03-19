from django.db import models
# from django.contrib.auth.models import Group
from django.contrib.auth.models import User

# Create your models here.
class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # tenant = Group.objects.get(name='tenant') 
    # user.groups.add(tenant)
    bank_account_number = models.IntegerField()
    emergency_contact= models.IntegerField()
    id_number= models.CharField(max_length=50)
    phone_number= models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    date_of_entry = models.DateTimeField(auto_now=True)