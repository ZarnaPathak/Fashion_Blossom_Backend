from django.urls import URLPattern,path
from . import views

urlpatterns = [
    path('dashboard',views.dashboard,name='dashboard'),
    path('address',views.address,name='address'),
    path('orders',views.orders,name='orders'),
    path('profile_details',views.profile_details,name='profile_details'),
]