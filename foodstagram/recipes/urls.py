from django.urls import path
from foodstagram.recipes.views import (RecipeDetailView, RecipeCreateView, RecipeUpdateView,
                                       RecipeDeleteView, UserRecipeListView, LikedRecipeListView)

urlpatterns = [
    path('<int:pk>/list/', UserRecipeListView.as_view(), name='recipe-list'),
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('create/', RecipeCreateView.as_view(), name='recipe-create'),
    path('<int:pk>/update/', RecipeUpdateView.as_view(), name='recipe-update'),
    path('<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('<int:pk>/liked/', LikedRecipeListView.as_view(), name='recipe-liked-list'),
]
