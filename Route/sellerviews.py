from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from Product.models import Product,ProductType
from django.contrib.auth.decorators import login_required
Seller = get_user_model()


@login_required(login_url='login')
def profile(request):
    try:
        seller = Seller.objects.get(id=request.user.id)
    except Seller.DoesNotExist:
        messages.error(request, "Seller profile not found.")
        return redirect("seller_login")

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")

        # Update only if value is provided
        seller.name = name.strip() if name else seller.name
        seller.email = email.strip() if email else seller.email
        seller.address = address.strip() if address else seller.address

        seller.save()
        messages.success(request, "Profile updated successfully.")
        return redirect("seller_profile")
    context={
        "seller":seller,
        "products":Product.objects.filter(seller=seller)
    }
    return render(request,"seller/profile.html",context)


@login_required(login_url="login")
def add_edit_product(request, product_id=None):
    seller = request.user
    product = None

    # If product_id exists → EDIT mode
    if product_id:
        product = Product.objects.get(id=product_id, seller=seller)

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        price = request.POST.get("price", "").strip()
        category_value = request.POST.get("category")
        description = request.POST.get("description", "").strip()
        image = request.FILES.get("image")

        # Validation
        if not title or not price or not category_value:
            messages.error(request, "Title, price, and category are required.")
        else:
            category =ProductType.objects.get(category=category_value)

            if product:
                # EDIT
                product.title = title
                product.price = price
                product.category = category
                product.description = description
                if image:
                    product.image = image
                product.save()

                messages.success(request, "Product updated successfully.")
            else:
                # ADD
                Product.objects.create(
                    seller=seller,
                    title=title,
                    price=price,
                    category=category,
                    description=description,
                    image=image
                )
                messages.success(request, "Product published successfully.")

            return redirect("seller_profile")

    context = {
        "product_category": ProductType.objects.all(),
        "product": product,   # None for add, object for edit
        "is_edit": bool(product),
    }
    return render(request, "seller/add_product.html", context)


@login_required(login_url="login")
def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect("seller_profile")