from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class FoodstagramUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class FoodstagramUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel
