from django.db import models
from cloudinary.uploader import destroy
from django.conf import settings


class ProductType(models.Model):
    category = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.category


class Product(models.Model):
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="products"
    )

    title = models.CharField(max_length=120)
    description = models.TextField()

    category = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
        null=True
    )

    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/")

    created_at = models.DateTimeField(auto_now_add=True)

   # -------------------------
    # DELETE OLD IMAGE ON REPLACE
    # -------------------------
    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old = Product.objects.get(pk=self.pk)
            except Product.DoesNotExist:
                old = None

            if old and old.image and old.image != self.image:
                destroy(old.image.name)

        super().save(*args, **kwargs)

    # -------------------------
    # DELETE IMAGE ON PRODUCT DELETE
    # -------------------------
    def delete(self, *args, **kwargs):
        if self.image:
            destroy(self.image.name)

        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title