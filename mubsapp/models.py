from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    cover = models.ImageField(upload_to='covers/')
    language = models.CharField(max_length=50)
    pdf = models.FileField(upload_to='books/pdfs/', null=True, blank=True)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

class SoftwareCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Software(models.Model):
    name = models.CharField(max_length=200)
    developer = models.CharField(max_length=100)
    release_date = models.DateField()
    version = models.CharField(max_length=50)
    license = models.CharField(max_length=50)
    platform = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='software_covers/')
    file = models.FileField(upload_to='software_files/')
    category = models.ForeignKey(SoftwareCategory, on_delete=models.CASCADE)
    size = models.FloatField(default=0.0)
    description = models.TextField(max_length=500, null=True, blank=True)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    content = models.TextField()
    duration = models.DurationField()
    youtube_link = models.URLField(blank=True, null=True)
    file = models.FileField(upload_to='tutorial_files/', blank=True, null=True)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.title


# Create Customer Profile
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	date_modified = models.DateTimeField(User, auto_now=True)
	phone = models.CharField(max_length=20, blank=True)
	address1 = models.CharField(max_length=200, blank=True)
	address2 = models.CharField(max_length=200, blank=True)
	city = models.CharField(max_length=200, blank=True)
	state = models.CharField(max_length=200, blank=True)
	zipcode = models.CharField(max_length=200, blank=True)
	country = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.user.username

# Create a user Profile by default when user signs up
def create_profile(sender, instance, created, **kwargs):
	if created:
		user_profile = Profile(user=instance)
		user_profile.save()

# Automate the profile thing
post_save.connect(create_profile, sender=User)