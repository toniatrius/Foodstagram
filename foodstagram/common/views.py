from django.shortcuts import redirect
from django.views.generic import ListView, TemplateView

from .models import RecipeLike
from ..recipes.models import Recipe


from django.http import JsonResponse


def like_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    user = request.user

    if user.is_authenticated:
        if user in recipe.likes.all():
            recipe.likes.remove(user)
        else:
            recipe.likes.add(user)

        # Redirect back to the same page after the like/unlike action
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        # Handle unauthenticated user case
        return JsonResponse({'error': 'User not authenticated'}, status=401)



# def like_recipe(request, pk):
#     recipe_like, created = RecipeLike.objects.get_or_create(user=request.user, recipe_id=pk)
#
#     if not created:
#         recipe_like.delete()
#
#     return redirect(request.META.get('HTTP_REFERER', '/'))


class IndexView(ListView):
    model = Recipe
    template_name = 'common/index.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')

        title = self.request.GET.get('title')
        category = self.request.GET.get('category')
        ingredients = self.request.GET.get('ingredients')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if category:
            queryset = queryset.filter(category__icontains=category)
        if ingredients:
            # Split the ingredients string by comma and space
            ingredients_list = ingredients.split(', ')
            # Filter queryset based on each ingredient
            for ingredient in ingredients_list:
                queryset = queryset.filter(ingredients__icontains=ingredient)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = context['object_list']

        # Iterate through queryset to split ingredients string into list
        for recipe in queryset:
            recipe.ingredients = recipe.ingredients.split(', ')

            recipe.like_count = recipe.likes.count()

            # Check if the user has liked the recipe
            recipe.liked = self.request.user in recipe.likes.all() if self.request.user.is_authenticated else False

        context['object_list'] = queryset
        return context


class Custom404View(TemplateView):
    template_name = '404.html'
