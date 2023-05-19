from django.db import models
from django.contrib.auth.models import User, auth
from datetime import date
from Product.models import Product
# Create your models here.
class Shipping_Address(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    address=models.CharField(max_length=300)
    zipcode=models.CharField(max_length=10)
    country=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    phone_no=models.CharField(max_length=12)

class Order(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    address=models.ForeignKey(Shipping_Address,on_delete=models.SET_NULL, null=True)
    date=models.DateField(default=date.today)
    tot_price=models.IntegerField()
    status=(
        ('Procssing','Procssing'),
        ('Pending','Pending'),
        ('Delivered','Delivered'),
        ('Canceled','Canceled')
    )
    status=models.CharField(max_length=30,default=" ",choices=status,blank=True)

class Order_Items(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE,null=True,blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    prod_color=models.CharField(max_length=10)
    prod_size=models.CharField(max_length=10)
    prod_qty=models.IntegerField()
    total=models.BigIntegerField()

class Payment(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    pay_type=models.CharField(max_length=10, null=True, blank=True)
    amount=models.IntegerField(default=0)
    is_paid=models.BooleanField(default=False)
    razor_pay_order_id = models.CharField(max_length=100, null=True, blank=True)