from django.contrib import admin
from .models import Book, Software, SoftwareCategory, Tutorial

admin.site.site_header = "BrainyToes Admin"
admin.site.site_title = "BrainyToes Admin Portal"
admin.site.index_title = "Welcome to BrainyToes Admin"

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pdf')

admin.site.register(Book, BookAdmin)
admin.site.register(Software)
admin.site.register(Tutorial)
admin.site.register(SoftwareCategory)
