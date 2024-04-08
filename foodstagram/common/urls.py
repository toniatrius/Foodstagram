from django.urls import path
from foodstagram.common.views import like_recipe, IndexView, Custom404View

handler404 = Custom404View.as_view()

app_name = 'common'

urlpatterns = [
    path('like/<int:pk>/', like_recipe, name='like-recipe'),
    path('', IndexView.as_view(), name='index'),
]
