from django.db import models

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

    def __str__(self):
        return self.title

class Software(models.Model):
    name = models.CharField(max_length=200)
    developer = models.CharField(max_length=100)
    release_date = models.DateField()
    version = models.CharField(max_length=50)
    license = models.CharField(max_length=50)
    platform = models.CharField(max_length=50)
    file = models.FileField(upload_to='software_files/')

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

    def __str__(self):
        return self.title
