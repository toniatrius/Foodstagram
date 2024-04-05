from django.urls import path
from foodstagram.accounts.views import (SignInUserView, SignUpUserView, signout_user, ProfileDetailsView,
                                        ProfileUpdateView, ProfileDeleteView)


urlpatterns = [
    path('signin/', SignInUserView.as_view(), name='signin'),
    path('signup/', SignUpUserView.as_view(), name='signup'),
    path('signout/', signout_user, name='signout'),
    path('profile/<int:pk>/', ProfileDetailsView.as_view(), name='profile'),
    path('profile/<int:pk>/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile-delete'),
]