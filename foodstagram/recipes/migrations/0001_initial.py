# Generated by Django 5.0.3 on 2024-04-04 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('instructions', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='recipes/')),
                ('category', models.CharField(max_length=100)),
                ('ingredients', models.ManyToManyField(to='recipes.ingredient')),
            ],
        ),
    ]
