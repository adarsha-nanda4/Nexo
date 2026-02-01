from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from Seller.models import Seller

def seller_login(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        try:
            seller=Seller.objects.get(phone=phone)

            user = authenticate(request, username=seller.username, password=password)

            if user is not None:
                auth_login(request, user)

                if user.is_staff:
                    return redirect("dashboard")

                return redirect("dashboard")
        except Exception as e:
            messages.error(request, e)

    return render(request, "login/login.html")


def seller_logout(request):
    auth_logout(request)
    return redirect("login")
