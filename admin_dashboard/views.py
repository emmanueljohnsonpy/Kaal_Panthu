from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.
def admin_login_view(request):
    return render(request, 'admin_dashboard/page-account-login.html')

def products_view(request):
    return render(request, 'admin_dashboard/page-products-list.html')

def users_view(request):
    return render(request, 'admin_dashboard/page-sellers-list.html')

def categories_view(request):
    return render(request, 'admin_dashboard/page-categories.html')
