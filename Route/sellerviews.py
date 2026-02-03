from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.db import IntegrityError
Seller = get_user_model()



def profile(request):
    return render(request,"seller/profile.html")