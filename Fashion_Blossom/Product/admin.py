from django.contrib import admin
from django.contrib.admin.sites import site
from .models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ColorVarient)
admin.site.register(SizeVariant)
admin.site.register(Product)
admin.site.register(Wishlist)