from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('admin/', include('admin_dashboard.urls')),
    path('', include('home.urls')), 
    path('home/', include('home.urls')),
    path('account/', include('account.urls')),
    path('shop/', include('shop.urls')),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
]