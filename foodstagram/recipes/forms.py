from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'instructions', 'photo', 'category', 'ingredients']

    def clean_ingredients(self):
        ingredients = self.cleaned_data['ingredients']
        if len(set(ingredients)) != len(ingredients):
            raise forms.ValidationError("Ingredients must be unique.")
        return ingredients
