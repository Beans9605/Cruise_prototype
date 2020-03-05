from django.shortcuts import render, get_object_or_404, redirect
from mainsite.models import User

# Create your views here.

def sign_up (request) :
    return render(request, 'login/sign.html')

def sign_up_indata (request) :
    username = request.POST.get('username')
    password = request.POST.get('pwd')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    gender = request.POST.get('gender')
    birthday = request.POST.get('birth')
    firstname = request.POST.get('Fname')
    lastname = request.POST.get('Lname')

    


def sign_in (request) :
    return render(request, 'login/login.html')