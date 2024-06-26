from django.contrib import admin
from . import models


class CartModelAdmin(admin.ModelAdmin):
    """
    Admin class for the Cart model.
    """

    pass


class CartItemModelAdmin(admin.ModelAdmin):
    """
    Admin class for the CartItem model.
    """

    pass


admin.site.register(models.Cart, CartModelAdmin)
admin.site.register(models.CartItem, CartItemModelAdmin)
