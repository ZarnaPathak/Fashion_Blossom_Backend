from django.urls import URLPattern,path
from . import views

urlpatterns = [
    path('checkout',views.checkout,name='checkout'),
]