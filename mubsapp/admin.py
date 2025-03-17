from django.contrib import admin
from .models import Book, Software, SoftwareCategory, Tutorial

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pdf')

admin.site.register(Book, BookAdmin)
admin.site.register(Software)
admin.site.register(Tutorial)
admin.site.register(SoftwareCategory)
