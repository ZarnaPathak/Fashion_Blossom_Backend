from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')

def address(request):
    return render(request,'address.html')

def orders(request):
    return render(request,'order.html')

def profile_details(request):
    return render(request,'profile-details.html')