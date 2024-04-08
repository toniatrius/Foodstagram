from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'instructions', 'photo', 'category', 'ingredients']
        labels = {
            'ingredients': 'Ingredients (separated by commas)'
        }
        help_texts = {
            'ingredients': 'Enter ingredients separated by commas, e.g., ingredient1, ingredient2, ingredient3'
        }
