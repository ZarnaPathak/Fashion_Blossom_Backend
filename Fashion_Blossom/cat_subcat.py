from Product.models import Category,SubCategory

def display():
    cat=Category.objects.all()
    subcat=SubCategory.objects.all()
    context={
        'cats':cat,
        'subcats':subcat,
    }
    return context