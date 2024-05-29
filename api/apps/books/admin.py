from django.contrib import admin
from . import models


class AuthorAdmin(admin.ModelAdmin):
    """
    Admin class for the Author model.
    """

    pass


class GenreAdmin(admin.ModelAdmin):
    """
    Admin class for the Genre model.
    """

    pass


class BookAdmin(admin.ModelAdmin):
    """
    Admin class for the Book model.
    """

    pass


admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Book, BookAdmin)
