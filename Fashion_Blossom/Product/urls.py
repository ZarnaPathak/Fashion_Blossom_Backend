from django.urls import URLPattern,path
from . import views

urlpatterns = [
    path('wishlist',views.wishlist,name='wishlist'),
]