# Generated by Django 5.1.7 on 2025-03-22 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mubsapp', '0014_remove_profile_old_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='softwarecategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_images/'),
        ),
    ]
