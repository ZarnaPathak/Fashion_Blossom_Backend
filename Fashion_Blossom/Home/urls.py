from django.urls import URLPattern,path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('shop',views.shop,name='shop'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('confirmation',views.confirmation,name='confirmation'),
    path('faq',views.faq,name='faq'),
    path('error',views.error,name='error'),
]
