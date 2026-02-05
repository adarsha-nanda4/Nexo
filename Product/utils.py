# Product/utils.py

import random
from decimal import Decimal
from django.contrib.auth import get_user_model

from .models import Product, ProductType

User = get_user_model()


DEFAULT_CATEGORIES = [
    "Electronics",
    "Fashion",
    "Home & Kitchen",
    "Books",
    "Sports",
    "Toys",
    "Grocery",
]


def generate_mock_products(count=150):
    users = list(User.objects.all())

    if not users:
        raise Exception("❌ No users found. Create at least one seller.")

    # ✅ Ensure ProductType exists
    categories = list(ProductType.objects.all())
    if not categories:
        categories = [
            ProductType.objects.create(category=name)
            for name in DEFAULT_CATEGORIES
        ]

    products = []

    for i in range(1, count + 1):
        products.append(
            Product(
                seller=random.choice(users),
                title=f"Mock Product {i}",
                description=f"Auto-generated description for product {i}",
                category=random.choice(categories),
                price=Decimal(random.randint(100, 5000)),
                # ✅ Cloudinary-safe existing image path
                image="products/ezgif-frame-003_lzxbdz.png",
            )
        )

    Product.objects.bulk_create(products)
    return f"✅ {count} mock products created"
