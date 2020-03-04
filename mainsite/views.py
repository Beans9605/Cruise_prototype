from django.shortcuts import render

# Create your views here.

def main_home(request) :
    return render(request, "mainsite/home.html")

def access_home(request) :
    return render(request, "mainsite/access_home.html")

def intro_compose(request) :
    return render(request, "mainsite/intro.html")

