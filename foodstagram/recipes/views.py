from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from foodstagram.recipes.forms import RecipeForm
from foodstagram.recipes.models import Recipe


class OwnerRequiredMixin(AccessMixin):
    """Verify that the current user has this profile."""
    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs.get('pk', None):
            return self.handle_no_permission()
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


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('common:index')  # Assuming 'home' is the name of your home page URL pattern


class RecipeUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_update.html'

    def get_success_url(self):
        return reverse_lazy('recipe-detail', kwargs={'pk': self.object.pk})


class RecipeDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy('home')
    template_name = 'recipes/recipe_delete.html'
