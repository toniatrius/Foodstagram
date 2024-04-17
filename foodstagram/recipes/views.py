from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from foodstagram.recipes.forms import RecipeForm
from foodstagram.recipes.models import Recipe


class OwnerRequiredMixin(View):
    """Verify that the current user is the author of the recipe."""
    def dispatch(self, request, *args, **kwargs):
        # Get the recipe object
        recipe = Recipe.objects.get(pk=kwargs.get('pk'))

        # Check if the logged-in user is the author of the recipe
        if request.user != recipe.author:
            raise Http404("You are not the owner of this recipe.")

        # If the user is the author, proceed with the view
        return super().dispatch(request, *args, **kwargs)


class UserRecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    paginate_by = 10

    def get_queryset(self):
        # Get the current user
        user_pk = self.request.user.pk

        # Filter recipes by the current user's primary key
        queryset = Recipe.objects.filter(author__pk=user_pk)

        return queryset


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ingredients = self.object.ingredients.split(', ')
        context['ingredients'] = ingredients
        return context


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('common:index')


class RecipeUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_update.html'

    def get_success_url(self):
        return reverse_lazy('recipe-detail', kwargs={'pk': self.object.pk})


class RecipeDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy('common:index')
    template_name = 'recipes/recipe_delete.html'


class LikedRecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipes_liked.html'
    paginate_by = 10

    def get_queryset(self):
        # Get the current user
        current_user = self.request.user
        # Filter recipes by the current user's liked recipes
        queryset = Recipe.objects.filter(likes=current_user)
        return queryset
