from django.shortcuts import render
from django.http import HttpResponse

def signup_login(request):
    return render(request, 'account/page-login-register.html')
