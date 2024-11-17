from django.urls import path
from .views import admin_login_view, products_view, users_view, categories_view

urlpatterns = [
    path("", admin_login_view, name="login"),
    path("products/", products_view, name="products_view"),
    path("users/", users_view, name="users_view"),
    path("categories/", categories_view, name="categories_view")
]