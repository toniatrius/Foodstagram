from django.urls import path
from foodstagram.common.views import like_recipe, IndexView

app_name = 'common'

urlpatterns = [
    path('like/<int:pk>/', like_recipe, name='like-recipe'),
    path('', IndexView.as_view(), name='index'),
]
