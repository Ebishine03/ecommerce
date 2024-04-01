from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Customer
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def account(request):
    print(request.POST)
    if request.POST and 'register' in request.POST:
      try:
        
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        password=request.POST.get('password')
        user=User.objects.create(username=name,password=password,email=email)

        Customer.objects.create(user=user,phone=phone,address=address)
        return redirect('home')
      except Exception as e:
         error_message="Dupilicate username"
         messages.error(request,error_message)
    if request.POST and 'login' in request.POST:
        name=request.POST.get('name')
        password=request.POST.get('password')
        user=authenticate(username=name,password=password)
        if user:
           login(request,user)
           return  redirect('home')
        else:
           messages.error('Inavlid credentials')

    return render(request,'account.html')
def signout(request):
   logout(request)
   return redirect('home')