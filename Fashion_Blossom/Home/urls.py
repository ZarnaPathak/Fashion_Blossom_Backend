from django.urls import URLPattern,path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('shop',views.shop,name='shop'),
]
