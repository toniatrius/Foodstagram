# Generated by Django 5.0.3 on 2024-04-16 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_recipe_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='recipe_photos/'),
        ),
    ]
