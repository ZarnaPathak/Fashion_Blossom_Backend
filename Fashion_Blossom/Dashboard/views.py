from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
from .form import *
from Order.models import *
from cat_subcat import display
# Create your views here.
def dashboard(request):
    data={
         'order':Order.objects.filter(user_id=request.user.id),
         'context':display()
    }
    return render(request,'dashboard.html',data)

def address(request):
    data={
        'address':Shipping_Address.objects.filter(user_id=request.user.id),
        'context':display()
    }
    return render(request,'address.html',data)

def orders(request):
    data={
         'order':Order.objects.filter(user_id=request.user.id),
         'context':display()
    }
    return render(request,'order.html',data)

def profile_details(request):
    adds=Shipping_Address.objects.filter(user_id=request.user.id)
    if adds.count()==0:
        add=Shipping_Address.objects.filter(user_id=request.user.id)
    else:
        add=adds[0]
    data={
        'add':add,
        'context':display()
    }
    return render(request,'profile-details.html',data)

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