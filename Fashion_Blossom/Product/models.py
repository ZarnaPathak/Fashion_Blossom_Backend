from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name=models.CharField(max_length=50)
    categories=models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    def cat_name(self):
        return self.categories.name

class ColorVarient(models.Model):
    name=models.CharField(max_length=30)
    code=models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    
class SizeVariant(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    product_name=models.CharField(max_length=50)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    subcategory=models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    color_variant=models.ManyToManyField(ColorVarient, blank=True)
    size_variant=models.ManyToManyField(SizeVariant, blank=True)
    img1=models.ImageField(upload_to='Product_images')
    img2=models.ImageField(upload_to='Product_images')
    img3=models.ImageField(upload_to='Product_images')

class Wishlist(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def img1(self):
        return self.product.img1
    def product_name(self):
        return self.product.product_name
    def price(self):
        return self.product.price