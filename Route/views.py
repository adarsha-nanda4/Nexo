from django.shortcuts import render,redirect
from Product.models import Product,ProductType
from django.db.models.functions import Random

def dashboard(request):
    context={
        "products": Product.objects.order_by("?")[:32],
        "product_category":ProductType.objects.all(),
    }
    return render(request,"dashboard.html",context)


def offline(request):
    return render(request, "offline.html")
