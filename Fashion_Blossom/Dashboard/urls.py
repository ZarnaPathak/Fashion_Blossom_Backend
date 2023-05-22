from django.urls import URLPattern,path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('dashboard',views.dashboard,name='dashboard'),
    path('address',views.address,name='address'),
    path('orders',views.orders,name='orders'),
    path('profile_details',views.profile_details,name='profile_details'),
    path('image_upload', views.avatarView, name = 'image_upload'),
    path('success', views.uploadok, name = 'success'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
