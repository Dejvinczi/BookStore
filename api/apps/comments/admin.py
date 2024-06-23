from django.contrib import admin
from . import models


class CommentAdmin(admin.ModelAdmin):
    """Admin class for the Comment model."""

    pass


admin.site.register(models.Comment, CommentAdmin)
