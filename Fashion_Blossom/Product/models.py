from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)

class SubCategory(models.Model):
    name=models.CharField(max_length=50)
    categories=models.ForeignKey(Category, on_delete=models.CASCADE)

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
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    color_variant=models.ManyToManyField(ColorVarient, blank=True)
    size_variant=models.ManyToManyField(SizeVariant, blank=True)
    img1=models.ImageField(upload_to='Product_images')
    img2=models.ImageField(upload_to='Product_images')
    img3=models.ImageField(upload_to='Product_images')