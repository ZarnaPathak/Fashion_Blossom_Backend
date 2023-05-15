from django.shortcuts import render

# Create your views here.
def wishlist(request):
    return render(request,'Wishlist.html')

def product_details(request):
    return render(request,'product-single.html')