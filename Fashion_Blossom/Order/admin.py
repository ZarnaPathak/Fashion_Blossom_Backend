from django.contrib import admin
from django.contrib.admin.sites import site
from .models import *
# Register your models here.
admin.site.register(Shipping_Address)
admin.site.register(Order)
admin.site.register(Order_Items)
admin.site.register(Payment)