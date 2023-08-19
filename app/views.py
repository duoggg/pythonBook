from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    doctors= Doctor.objects.all()
    context={'doctors': doctors}
    return render(request,'app/home.html',context)

def cart(request,doctor_id):
    try:
        doctor = Doctor.objects.get(pk=doctor_id)
    except Doctor.DoesNotExist:
        # Xử lý nếu không tìm thấy sản phẩm với product_id cụ thể
        # Ví dụ: return HttpResponse("Sản phẩm không tồn tại.")
        pass
    context={'doctor': doctor}
    return render(request,'app/index-infoDR.html',context)

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context ={'form':form}
    return render(request,'app/register.html',context)

def login(request):
    # doctors= Doctor.objects.all()
    # context={'doctors': doctors}
    context={}
    return render(request,'app/login.html',context)