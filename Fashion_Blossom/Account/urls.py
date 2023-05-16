from django.urls import URLPattern,path
from . import views

urlpatterns = [
    path('signin',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('forget_pass',views.forget_password,name='forget'),
]
