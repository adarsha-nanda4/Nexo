from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Seller


@admin.register(Seller)
class SellerAdmin(UserAdmin):
    model = Seller

    # REMOVE username completely
    fieldsets = (
        (None, {"fields": ("phone", "password")}),
        ("Personal info", {
            "fields": (
                "name",
                "email",
                "address",
                "id_proof",
                "is_verified",
            )
        }),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "phone",
                "name",
                "email",
                "password1",
                "password2",
            ),
        }),
    )

    list_display = ("phone", "name", "email", "is_verified", "is_staff")
    search_fields = ("phone", "email", "name")
    ordering = ("phone",)
