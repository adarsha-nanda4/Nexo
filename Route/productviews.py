from django.shortcuts import render
from Product.models import Product
# Create your views here.
def home(request):
    context={
        "products":Product.objects.all().order_by("created_at")
    }
    return render(request,"product/home.html",context)

def product_detail(request,pid):
    context={
        "product":Product.objects.get(pk=pid)
    }
    return render(request,"product/product_detail.html",context)