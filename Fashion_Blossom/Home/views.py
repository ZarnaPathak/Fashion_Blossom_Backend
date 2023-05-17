from django.shortcuts import render
from Product.models import Category,SubCategory
# Create your views here.
def home(request):
    cats=Category.objects.all()
    subcats=SubCategory.objects.all()
    ct={
        'cats':cats,
        'subcats':subcats
    }
    return render(request,'index.html',ct)

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def error(request):
    return render(request,'404.html')

def faq(request):
    return render(request,'faq.html')

def confirmation(request):
    return render(request,'confirmation.html')