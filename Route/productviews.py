from django.db.models import Q
from django.shortcuts import render
from Product.models import Product,ProductType
from django.db.models.functions import Random


def p_filter(request,cat):
    context={
        "products":Product.objects.filter(category=cat).order_by(Random()),
        "product_types":ProductType.objects.all().exclude(id=cat).order_by(Random()),
        "current_product_type":ProductType.objects.get(id=cat),
    }
    return render(request,"product/p_filter.html",context)



def p_search(request):
    query = request.GET.get("q", "").strip()

    products = Product.objects.select_related("category", "seller")

    if query:
        products = products.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(category__category__icontains=query)
        )

    return render(request, "product/p_search.html", {
        "products": products,
        "query": query
    })


def p_detail(request,pid):
    context={
        "product":Product.objects.get(pk=pid)
    }
    return render(request,"product/p_detail.html",context)