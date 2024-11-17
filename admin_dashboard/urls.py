from django.urls import path
from .views import admin_login_view, products_view

urlpatterns = [
    path("", admin_login_view, name="login"),
    path("products/", products_view, name="product_view")
]