from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_home, name="main_home"),
    path('intro/', views.intro_compose, name="intro_compose"),
    path('access/', views.access_home, name="access_home"),
]
