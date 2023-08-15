from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('cart/<int:doctor_id>/', views.cart,name="cart"),
    path('register', views.register,name="register"),
]