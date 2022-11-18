from tkinter import Widget
from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    username = models.CharField(max_length=150, unique=True)
    documento=models.CharField(max_length=10)
    nPersona= models.CharField(max_length=40,null=True)