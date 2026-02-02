from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.db import IntegrityError
Seller = get_user_model()


def registration(request):
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

            return render(request,"seller/reg_success.html")

        except IntegrityError:
            messages.error(request, "Phone number already registered.")
            return redirect("registration")

    return render(request,"seller/registration.html")

def profile(request):
    return render(request,"seller/profile.html")