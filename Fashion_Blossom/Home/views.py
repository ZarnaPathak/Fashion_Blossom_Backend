from django.shortcuts import render
from Product.models import Category,SubCategory,Product
from cat_subcat import display
# Create your views here.
def home(request):
    all_prod=Product.objects.all()
    trendy_prod=all_prod[:3]
    data={
        'trendy':trendy_prod,
        'context':display(),
    }
    return render(request,'index.html',data)

def contact(request):
    context=display()
    return render(request,'contact.html',context)

def about(request):
    context=display()
    return render(request,'about.html',context)

def error(request):
    context=display()
    return render(request,'404.html',context)

def faq(request):
    context=display()
    return render(request,'faq.html',context)

def confirmation(request):
    context=display()
    return render(request,'confirmation.html',context)
