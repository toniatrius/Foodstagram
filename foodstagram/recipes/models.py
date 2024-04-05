from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

UserModel = get_user_model()


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    MAX_LEN_NAME = 255
    MIN_LEN_NAME = 2
    MAX_LEN_DESCRIPTION = 1000
    MAX_LEN_INSTRUCTIONS = 2000
    MAX_LEN_CATEGORY = 100

    name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=[MinLengthValidator(MIN_LEN_NAME)],
        verbose_name='Name',
        null=False,
        blank=False,
    )

    description = models.TextField(
        max_length=MAX_LEN_DESCRIPTION,
        verbose_name='Description',
        null=False,
        blank=False,
    )

    instructions = models.TextField(
        max_length=MAX_LEN_INSTRUCTIONS,
        verbose_name='Instructions',
        null=False,
        blank=False,
    )

    photo = models.ImageField(
        upload_to='recipes/',
        blank=False,
        null=True,
        verbose_name='Photo',
    )

    category = models.CharField(
        max_length=MAX_LEN_CATEGORY,
        verbose_name='Category',
        null=False,
        blank=False,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    ingredients = models.ManyToManyField(
        Ingredient,
        verbose_name='Ingredients',
    )

    author = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        default=None,
        verbose_name='Author',
    )

    def __str__(self):
        return self.name
