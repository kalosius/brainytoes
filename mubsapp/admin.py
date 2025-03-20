from django.contrib import admin
from .models import Book, Software, SoftwareCategory, Tutorial,Profile
from django.contrib.auth.models import User

admin.site.site_header = "BrainyToes Admin"
admin.site.site_title = "BrainyToes Admin Portal"
admin.site.index_title = "Welcome to BrainyToes Admin"

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pdf')

admin.site.register(Book, BookAdmin)
admin.site.register(Software)
admin.site.register(Tutorial)
admin.site.register(SoftwareCategory)
admin.site.register(Profile)



# Mix profile info and user info
class ProfileInline(admin.StackedInline):
	model = Profile

# Extend User Model
class UserAdmin(admin.ModelAdmin):
	model = User
	field = ["username", "first_name", "last_name", "email"]
	inlines = [ProfileInline]

# Unregister the old way
admin.site.unregister(User)

# Re-Register the new way
admin.site.register(User, UserAdmin)