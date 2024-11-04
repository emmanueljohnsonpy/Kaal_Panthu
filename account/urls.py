from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signup_login, name='signup_login')
]