# Product/utils.py

import random
import base64
from decimal import Decimal
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile

from .models import Product, ProductType

User = get_user_model()


# 1x1 transparent PNG (VALID IMAGE)
DUMMY_IMAGE_BASE64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGNgYAAAAAMAASsJTYQAAAAASUVORK5CYII="
)


def generate_mock_products(count=150):
    users = list(User.objects.all())
    categories = list(ProductType.objects.all())

    if not users:
        raise Exception("❌ No users found. Create at least one seller.")

    if not categories:
        raise Exception("❌ No ProductType found.")

    image_bytes = base64.b64decode(DUMMY_IMAGE_BASE64)

    products = []

    for i in range(1, count + 1):
        product = Product(
            seller=random.choice(users),
            title=f"Mock Product {i}",
            description=f"Auto-generated description for product {i}",
            category=random.choice(categories),
            price=Decimal(random.randint(100, 5000)),
        )

        # ✅ VALID image for Cloudinary
        product.image.save(
            f"product_{i}.png",
            ContentFile(image_bytes),
            save=False
        )

        products.append(product)

    Product.objects.bulk_create(products)
    return count
