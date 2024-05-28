from django.contrib import admin
from . import models

class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Book, BookAdmin)
