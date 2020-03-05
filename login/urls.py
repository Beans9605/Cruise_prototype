from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.sign_up, name="sign_up"),
    path('login/', views.sign_in, name="sign_in"),
]
