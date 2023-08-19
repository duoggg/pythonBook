from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('cart/<int:doctor_id>/', views.cart,name="cart"),
    path('register', views.register,name="register"),
    path('login', views.loginPage,name="login"),
    path('logout', views.logoutPage,name="logout"),
    path('order/<int:doctor_id>/<int:shift>/<str:date>/',views.order,name="order"),
]