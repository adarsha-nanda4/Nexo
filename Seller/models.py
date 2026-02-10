from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class SellerManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError("Phone number is required")

        extra_fields.setdefault("is_active", True)

        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(phone, password, **extra_fields)



class Seller(AbstractUser):
    username = None  

    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=200)
    id_proof = models.ImageField(upload_to="seller/id_proof")
    is_verified = models.BooleanField(default=False)

    objects = SellerManager()  

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["email", "name"]

    def __str__(self):
        return f"{self.phone} - {self.name}"
