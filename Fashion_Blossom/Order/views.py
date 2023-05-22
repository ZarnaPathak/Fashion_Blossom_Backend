from django.shortcuts import render,redirect,HttpResponse
from .models import *
from Product.models import Product
from Fashion_Blossom.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
from django.conf import settings
import razorpay
client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET_KEY))
# Create your views here.
def item_add(request):
    u_id=request.user.id
    pid=request.POST.get('pid')
    color=request.POST.get('p_color')
    size=request.POST.get('p_size')
    qty=request.POST.get('product-quantity')
    prod=Product.objects.get(id=pid)
    prc=prod.price
    total=prc*int(qty)
    obj=Order_Items(user_id=u_id, product_id=pid, prod_color=color, prod_size=size, prod_qty=qty, total=total)
    obj.save()
    item=Order_Items.objects.get(id=obj.id)
    return render(request,'checkout.html',{'item':item})

def item_remove(request,odr_itm_id):
    order_item=Order_Items.objects.get(id=odr_itm_id)
    order_item.delete()
    return redirect('/')

def shipping_details(request):
    uid=request.user.id
    address=request.POST.get('address')
    zipcode=request.POST.get('zipcode')
    country=request.POST.get('country')
    state=request.POST.get('state')
    city=request.POST.get('city')
    phone=request.POST.get('phone')
    if Shipping_Address.objects.filter(user_id=uid,zipcode=zipcode).exists():
        return HttpResponse('Details Already Exist..')
    else:
        details=Shipping_Address(user_id=uid,address=address,zipcode=zipcode,country=country,state=state,city=city,phone_no=phone)
        details.save()
        addid=details.id
        return HttpResponse(addid)
    
def place_order(request):
    u_id=request.user.id
    odr_item_id=request.POST.get('odr_itm_id')
    address=request.POST.get('address')
    total_price=request.POST.get('tot')
    pay_type=request.POST.get('pay')
    porder=Order(user_id=u_id,address_id=address,tot_price=total_price,pay_type=pay_type)
    porder.save()
    od=Order_Items.objects.get(id=odr_item_id)
    od.order_id=porder.id
    od.save()
    order=Order.objects.get(id=porder.id)
    Payment.amount = od.total*100
    order_currency = 'INR'
    payment_order= client.order.create({'amount':Payment.amount, 'currency':order_currency, 'payment_capture': 1})
    Payment.razor_pay_order_id = payment_order['id']
    context = {
        'total':Payment.amount,
        'amount' : 500, 
        'api_key':RAZORPAY_API_KEY, 
        'payment_order': payment_order,
        'order_id': Payment.razor_pay_order_id,
        'order':order
    }
    return render(request,'Payment.html',context)

def success(request):
    order_id = request.GET.get('order_id')
    total=request.GET.get('amount')
    p_order=request.GET.get('p_order')
    pay = Payment(razor_pay_order_id = order_id)
    pay.is_paid = True
    pay.amount=int(total)
    pay.order_id=p_order
    pay.save()
    return render(request,'confirmation.html')

def payment(request):
    return render(request,'confirmation.html')
   
def checkout(request):
    return render(request,'checkout.html')
