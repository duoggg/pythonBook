from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.
class Doctor(models.Model):
    #  doctor_id = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=False)
     name = models.CharField(max_length=200,null=True)
     special=models.CharField(max_length=200,null=True)
     
     def __str__(self): 
         return self.name
     
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
# class Product(models.Model):
#     name=models.CharField(max_length=200,null=True)
#     price=models.FloatField(max_length=200,null=True)
#     digital = models.BooleanField(default=False,null=True,blank=False)

#     def __str__(self): 
#         return self.name
    
# class Order(models.Model):
#     customer=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
#     doctor = models.ForeignKey(Doctor,on_delete=models.SET_NULL,blank=True,null=True)

#     name=models.CharField(max_length=200,null=True)
#     price=models.FloatField(max_length=200,null=True)
#     complete = models.BooleanField(default=False,null=True,blank=False)
#     transaction_id=models.CharField(max_length=200,null=True)

#     def __str__(self): 
#         return str(self.id)
