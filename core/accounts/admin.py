from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import CustomUserModel, Profile

# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUserModel
    list_display = (
        "email",
        "is_superuser",

    )
    list_filter = (
        "email",
        "is_superuser",

    )
    search_fields = ("email",)
    ordering = ("email",)
    fieldsets = (
        ("Authentication", {"fields": ("email", "password")}),
        (
            "Permission",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (
            " group Permission",
            {
                "fields": (
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("important date", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",

                )
            },
        ),
    )


admin.site.register(CustomUserModel, CustomUserAdmin)
admin.site.register(Profile)
