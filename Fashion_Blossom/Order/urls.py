from django.urls import URLPattern,path
from . import views

urlpatterns = [
    path('checkout',views.checkout,name='checkout'),
    path('add_item',views.item_add,name='add_item'),
    path('item_remove<int:odr_itm_id>',views.item_remove,name='item_remove'),
    path('shipping',views.shipping_details,name='shipping_details'),
    path('place_order',views.place_order,name="place_order"),
]
