from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
from .form import *
from Order.models import *
# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')

def address(request):
    add=Shipping_Address.objects.filter(user_id=request.user.id)
    return render(request,'address.html',{'address':add})

def orders(request):
    od=Order.objects.filter(user_id=request.user.id)
    return render(request,'order.html',{'order':od})

def profile_details(request):
    add=Shipping_Address.objects.get(user_id=request.user.id)
    return render(request,'profile-details.html',{'add':add})

def avatarView(request):
  
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ProfileForm()
    return render(request, 'dashboard.html', {'form' : form})
    
def uploadok(request):
    return render(request,'profile-details.html')