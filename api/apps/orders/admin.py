from django.contrib import admin
from . import models


class OrderAdmin(admin.ModelAdmin):
    """Admin class for the Order model."""

    pass


class OrderItemAdmin(admin.ModelAdmin):
    """Admin class for the OrderItem model."""

    pass


admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderItem, OrderItemAdmin)
