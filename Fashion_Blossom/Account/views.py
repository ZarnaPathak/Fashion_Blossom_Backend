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
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('password') 
        if username=='' and password=='':
            data={
                    'error':True,
                    'msg':'Please enter username and password.',
                }
            return render(request,'login.html',data) 
        elif username=='':
            data={
                    'error':True,
                    'msg':'Please enter username.',
                }
            return render(request,'login.html',data) 
        elif password=='':
            data={
                    'error':True,
                    'msg':'Please enter password.',
                }
            return render(request,'login.html',data)
        else:
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                data={
                    'error':True,
                    'msg':'Invalid Username and password',
                }
                return render(request,'login.html',data)
            
    else:
     return render(request,'login.html')

def forget_password(request):
    return render(request,'forget-password.html')