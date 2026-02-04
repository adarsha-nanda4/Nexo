from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from Seller.models import Seller
from django.db import IntegrityError



def registration(request):
    if request.user.is_authenticated:
        return redirect("seller_profile")
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address = request.POST.get("address")
        password = request.POST.get("password")
        id_proof = request.FILES.get("id_proof")


        if not all([name, email,phone, address, password, id_proof]):
            messages.error(request, "All fields are required.")
            return redirect("registration")

        try:
            seller = Seller.objects.create_user(
                username=phone,         
                password=password,
                phone=phone,
                email=email,
                name=name,
                address=address,
                id_proof=id_proof,
                is_verified=False,
            )

            return render(request,"login/s_reg_success.html")

        except IntegrityError:
            messages.error(request, "Phone number already registered.")
            return redirect("registration")

    return render(request,"login/s_registration.html")

def seller_login(request):
    if request.user.is_authenticated:
        return redirect("seller_profile")

    if request.method == 'POST':
        print("reached here")
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        try:
            seller=Seller.objects.get(phone=phone)
            user = authenticate(request, username=seller.username, password=password)
            if user is not None:
                auth_login(request, user)

                if user.is_staff:
                    return redirect("seller_profile")

                return redirect("seller_profile")
        except Exception as e:
            messages.error(request, e)

    return render(request, "login/s_login.html")


def seller_logout(request):
    auth_logout(request)
    return redirect("login")
