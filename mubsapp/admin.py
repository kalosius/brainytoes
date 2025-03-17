from django.contrib import admin
from .models import Book, Software, Tutorial

# Register your models here.
admin.site.register(Book)
admin.site.register(Software)
admin.site.register(Tutorial)
