from django.shortcuts import redirect
from django.views.generic import ListView

from .models import RecipeLike
from ..recipes.models import Recipe


def like_recipe(request, pk):
    recipe_like, created = RecipeLike.objects.get_or_create(user=request.user, recipe_id=pk)

    if not created:
        recipe_like.delete()

    return redirect(request.META.get('HTTP_REFERER', '/'))


class IndexView(ListView):
    model = Recipe
    template_name = 'common/index.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        # Perform search based on query parameters
        title = self.request.GET.get('title')
        category = self.request.GET.get('category')
        ingredients = self.request.GET.get('ingredients')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if category:
            queryset = queryset.filter(category__icontains=category)
        if ingredients:
            queryset = queryset.filter(ingredients__name__icontains=ingredients)

        return queryset
