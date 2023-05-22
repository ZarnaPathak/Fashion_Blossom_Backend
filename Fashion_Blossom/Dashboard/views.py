from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
from .form import *
# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')

def address(request):
    return render(request,'address.html')

def orders(request):
    return render(request,'order.html')

def profile_details(request):
    return render(request,'profile-details.html')

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