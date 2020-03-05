from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser
# Create your models here.

class Room (models.Model) :
    location = models.CharField(max_length=20, blank=True)

class Cruise (models.Model) :
    room = models.ManyToManyField(Room)
    inside_map = models.ImageField(upload_to="mainsite/cruise/inside_map", blank=True)

class User (AbstractUser) :
    birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True)
    location = models.CharField(max_length=30, blank=True)
    usercode = models.CharField(max_length=5, blank=True)
    cruise = models.ForeignKey(Cruise, on_delete=models.CASCADE, blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    position = models.CharField(max_length=20, blank=True)
    phoneNumber = models.CharField(max_length=20, blank=True)