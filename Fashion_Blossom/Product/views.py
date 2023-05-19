from django.shortcuts import render,redirect
from .models import Product,Wishlist,SizeVariant,ColorVarient
from django.contrib.auth.models import User
# Create your views here.
def shop(request,sid):
    prods=Product.objects.filter(subcategory=sid)
    return render(request,'shop.html',{'Products':prods})

def wishlist(request):
    u_id=request.user.id
    wish_item=Wishlist.objects.filter(user_id=u_id)
    return render(request,'Wishlist.html', {'wish_item':wish_item})

def add_to_wish(request,pid):
    u_id=request.user.id
    if Wishlist.objects.filter(user_id=u_id,product_id=pid).exists():
        return redirect('wishlist')
    else:
        Wishlist.objects.create(product_id=pid,user_id=u_id)
        return redirect('wishlist')

def remove_wish(request,wid):
    rm_wish_prod=Wishlist.objects.get(id=wid)
    rm_wish_prod.delete()
    return redirect('wishlist')

def cart(request):
    return render(request, 'cart.html')

def add_to_cart(request,pid):
    return render(request, 'cart.html')

def checkout(request):
    return render(request,'checkout.html')

def product_details(request,pid):
    prod_detail=Product.objects.get(id=pid)
    size=SizeVariant.objects.all()
    color=ColorVarient.objects.all()
    context={
        'data':prod_detail,
        'size':size,
        'color':color
    }
    return render(request,'product-single.html',context)