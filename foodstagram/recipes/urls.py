from django.urls import path
from foodstagram.recipes.views import (RecipeDetailView, RecipeCreateView, RecipeUpdateView,
                                       RecipeDeleteView, UserRecipeListView)


urlpatterns = [
    path('<int:pk>/list/', UserRecipeListView.as_view(), name='recipe-list'),
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('create/', RecipeCreateView.as_view(), name='recipe-create'),
    path('<int:pk>/update/', RecipeUpdateView.as_view(), name='recipe-update'),
    path('<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
]
