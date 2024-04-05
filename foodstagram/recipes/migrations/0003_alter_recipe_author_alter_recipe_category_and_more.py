# Generated by Django 5.0.3 on 2024-04-05 16:58

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_author'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(max_length=100, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='recipes.ingredient', verbose_name='Ingredients'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(max_length=2000, verbose_name='Instructions'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='recipes/', verbose_name='Photo'),
        ),
    ]
