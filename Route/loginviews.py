from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from Seller.models import Seller
from django.db import IntegrityError
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from Seller.models import Seller
from django.db import IntegrityError




def registration(request):
    if request.user.is_authenticated:
        return redirect("seller_profile")

    context = {
        "acerrors": False,
        "fileerrors": False,
    }

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address = request.POST.get("address")
        password = request.POST.get("password")
        id_proof = request.FILES.get("id_proof")

        if not all([name, phone, email, address, password, id_proof]):
            context["acerrors"] = True
            return render(request, "login/s_registration.html", context)

        try:
            with transaction.atomic():
                seller = Seller.objects.create_user(
                    phone=phone,
                    password=password,
                    email=email,
                    name=name,
                    address=address,
                    id_proof=id_proof,
                    is_verified=False,
                )

                # ✅ LOGIN but DON'T redirect to profile
                auth_login(request, seller)

            # ✅ Show success page instead
            return render(
                request,
                "login/s_reg_success.html",
                {"seller": seller},
            )

        except IntegrityError as e:
            print("INTEGRITY ERROR:", e)
            context["acerrors"] = True
            return render(request, "login/s_registration.html", context)

        except OSError as e:
            print("FILE ERROR:", e)
            context["fileerrors"] = True
            return render(request, "login/s_registration.html", context)

    return render(request, "login/s_registration.html", context)

def seller_login(request):
    if request.user.is_authenticated:
        return redirect("seller_profile")

    context = {
        "acerror": False,   
        "perror": False,   
    }

    if request.method == "POST":
        phone = request.POST.get("phone")
        password = request.POST.get("password")

        try:
            seller = Seller.objects.get(phone=phone)
        except Seller.DoesNotExist:
            context["acerror"] = True
            return render(request, "login/s_login.html", context)

        user = authenticate(request, phone=phone, password=password)

        if user is None:
            context["perror"] = True
            return render(request, "login/s_login.html", context)

        auth_login(request, user)
        return redirect("seller_profile")

    return render(request, "login/s_login.html", context)

def seller_logout(request):
    auth_logout(request)
    return redirect("login")
