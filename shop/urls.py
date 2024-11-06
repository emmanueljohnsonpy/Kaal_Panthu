from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.shop_list, name='shoplist'),
    path('product-desc', views.product_desc, name='productdesc')
]