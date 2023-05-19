from django.urls import URLPattern,path
from . import views

urlpatterns = [
    path('shop<int:sid>',views.shop,name='shop'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('add_to_wish<int:pid>',views.add_to_wish,name='add_to_wish'),
    path('remove_wish<int:wid>',views.remove_wish,name='remove_wish'),
    path('cart',views.cart,name="cart"),
    path('checkout',views.checkout,name='checkout'),
    path('add_to_cart<int:pid>',views.add_to_cart,name="add_to_cart"),
    path('product_details<int:pid>',views.product_details,name='product_details'),
]