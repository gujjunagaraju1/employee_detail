from django.db import models

class Employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='images')
    designation=models.CharField(max_length=100)
    email_address=models.EmailField(max_length=100,unique=True)
    phone_number=models.CharField(max_length=15,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    
    

# Create your models here.
