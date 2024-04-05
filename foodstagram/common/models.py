from django.contrib.auth import get_user_model
from django.db import models
from foodstagram.recipes.models import Recipe

UserModel = get_user_model()


class RecipeLike(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ('recipe', 'user',)

