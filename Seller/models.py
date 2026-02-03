from django.contrib.auth.models import AbstractUser
from django.db import models


class Seller(AbstractUser):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=254)
    phone = models.CharField(max_length=15, unique=True)
    address=models.CharField(max_length=200)
    id_proof= models.ImageField(upload_to="seller/id_proof")
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(f"{self.username} - {self.name}")
