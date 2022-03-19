from django.db import models


from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number= models.CharField(max_length=50)
    phone_number= models.CharField(max_length=50)