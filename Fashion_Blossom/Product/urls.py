from django.urls import URLPattern,path
from . import views

urlpatterns = [
    path('wishlist',views.wishlist,name='wishlist'),
    path('product_details',views.product_details,name='product_details'),
]