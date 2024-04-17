from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.generic import ListView

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

        return redirect(request.META.get('HTTP_REFERER'))

    else:
        return JsonResponse({'error': 'User not authenticated'}, status=401)


class IndexView(ListView):
    model = Recipe
    template_name = 'common/index.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')

        search_query = self.request.GET.get('q')

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(category__icontains=search_query) |
                Q(ingredients__icontains=search_query)
            )

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


def error_404_view(request, exception):
    return render(request, '404.html', {})
