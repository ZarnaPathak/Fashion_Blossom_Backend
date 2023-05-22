from django.shortcuts import render,redirect
from .models import Product,Wishlist,SizeVariant,ColorVarient,Category
from django.contrib.auth.models import User
from cat_subcat import display
# Create your views here.
def shop(request,sid):
    data={
        'Products':Product.objects.filter(subcategory=sid),
        'context':display()
    }
    return render(request,'shop.html',data)

def cat_top(request,cid):
    data={
        'Products':Product.objects.filter(category_id=cid),
        'context':display()
    }
    return render(request,'shop.html',data)

def wishlist(request):
    u_id=request.user.id
    data={
        'wish_item':Wishlist.objects.filter(user_id=u_id),
        'context':display()
    }
    return render(request,'Wishlist.html',data)

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

def product_details(request,pid):
    prod_detail=Product.objects.get(id=pid)
    subid=prod_detail.subcategory_id
    sub_prod=Product.objects.filter(subcategory_id=subid)
    size=SizeVariant.objects.all()
    color=ColorVarient.objects.all()
    context={
        'data':prod_detail,
        'size':size,
        'color':color,
        'sub_prod':sub_prod,
        'context':display()
    }
    return render(request,'product-single.html',context)