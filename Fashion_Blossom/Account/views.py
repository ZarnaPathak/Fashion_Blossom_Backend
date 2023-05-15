from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import check_password

# Create your views here.
def register(request):
    if request.method == 'POST':
        firstname=request.POST['FirstName']
        lastname=request.POST['LastName']
        email=request.POST['Email']
        username=request.POST['Username']
        password=request.POST['Password1']
        password1=request.POST['Password2']

        if password==password1:
            if User.objects.filter(email=email).exists():
                data={
                    'error':True,
                    'msg':'Email exist.',
                }
                return render(request,'signin.html',data) 
            elif User.objects.filter(username=username).exists():
                data={
                    'error':True,
                    'msg':'Username exist.',
                }
                return render(request,'signin.html',data) 
            else:
                user=User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username,  password=password)
                user.save();
                print('user created')
                return render(request,'login.html')
            
        else:
            data={
                    'error':True,
                    'msg':'Password does not match.',
                }
            return render(request,'signin.html',data) 
            
    else:
        return render(request,'signin.html')


def login(request):
    return render(request,'login.html')

def forget_password(request):
    return render(request,'forget-password.html')