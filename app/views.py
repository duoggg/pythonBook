import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def home(request):
    doctors= Doctor.objects.all()
    context={'doctors': doctors}
    return render(request,'app/home.html',context)

def cart(request,doctor_id):
    try:
        doctor = Doctor.objects.get(pk=doctor_id)
        shift = 1
        dateOrder = '19/11/2003'
    except Doctor.DoesNotExist:
        # Xử lý nếu không tìm thấy sản phẩm với product_id cụ thể
        # Ví dụ: return HttpResponse("Sản phẩm không tồn tại.")
        pass
    
    context={'doctor': doctor,'shift':shift,'dateOrder':dateOrder}
    return render(request,'app/index-infoDR.html',context)

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context ={'form':form}
    return render(request,'app/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else: messages.info(request,'user or password not correct!')

    # doctors= Doctor.objects.all()
    # context={'doctors': doctors}
    context={}
    return render(request,'app/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def order(request):  
    if request.user.is_authenticated:
        data = json.loads(request.body)
        doctorId = data['doctorId']
        dateOrder = data['dateOrder']
        shift = data['shift']
        customer = request.user
        doctor = Doctor.objects.get(id= doctorId)
        date_obj = datetime.strptime(dateOrder, '%d/%m/%Y').date()
        order, created = Order.objects.get_or_create(customer= customer,doctor= doctor,shift=shift,date_appoint = date_obj)
        order.save()
        context={'order': order}
        return redirect('home')
    else : return redirect('login')
   

# def order(request,doctor_id):
#     try:
        # doctor = Doctor.objects.get(pk=doctor_id)
        # if request.user.is_authenticated:
        # # data = json.loads(request.body)
        # # doctorId = data['doctorId']
        # # dateOrder = data['dateOrder']
        # # shift = data['shift']
        #     customer = request.user
        #     doctor = Doctor.objects.get(id= doctor_id)
        #     date_obj = datetime.strptime(date, '%d/%m/%Y').date()
        #     order, created = Order.objects.get_or_create(customer= customer,doctor= doctor,shift=shift,date_appoint = date_obj)
        #     order.save()
        #     context={'order': order}
        #     return redirect('home')
        # else : return redirect('login')
    # except Doctor.DoesNotExist:
    #     # Xử lý nếu không tìm thấy sản phẩm với product_id cụ thể
    #     # Ví dụ: return HttpResponse("Sản phẩm không tồn tại.")
    #     pass
    # return redirect('home')
    
    
  
   

