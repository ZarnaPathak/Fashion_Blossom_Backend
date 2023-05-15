from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,'signin.html')

def login(request):
    return render(request,'login.html')

def forget_password(request):
    return render(request,'forget-password.html')