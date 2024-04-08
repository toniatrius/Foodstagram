from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'category', 'description', 'photo', 'created_at', 'updated_at')
    search_fields = ('name', 'description', 'category')
    list_filter = ('category',)
    list_per_page = 20  # Number of items per page
