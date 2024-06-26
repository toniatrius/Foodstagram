from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.shortcuts import redirect

from django.contrib.auth import views as auth_views, login, logout
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from foodstagram.accounts.forms import FoodstagramUserCreationForm
from foodstagram.accounts.models import Profile


class OwnerRequiredMixin(AccessMixin):
    """Verify that the current user has this profile."""
    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs.get('pk', None):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class SignInUserView(auth_views.LoginView):
    template_name = "accounts/log_in.html"
    redirect_authenticated_user = True


class SignUpUserView(views.CreateView):
    template_name = "accounts/sign_up.html"
    form_class = FoodstagramUserCreationForm
    success_url = reverse_lazy('common:index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)
        return result


def signout_user(request):
    logout(request)
    return redirect('common:index')


class ProfileDetailsView(LoginRequiredMixin, OwnerRequiredMixin, views.DetailView):
    queryset = Profile.objects.prefetch_related("user").all()
    template_name = "accounts/details_profile.html"


class ProfileUpdateView(LoginRequiredMixin, OwnerRequiredMixin, views.UpdateView):
    queryset = Profile.objects.all()
    template_name = "accounts/edit_profile.html"
    fields = ("first_name", "last_name", "date_of_birth", "profile_picture")

    def get_success_url(self):
        return reverse("profile", kwargs={"pk": self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields["date_of_birth"].widget.attrs["type"] = "date"
        form.fields["date_of_birth"].label = "Birthday"
        return form


class ProfileDeleteView(LoginRequiredMixin, OwnerRequiredMixin, views.DeleteView):
    queryset = Profile.objects.all()
    template_name = "accounts/delete_profile.html"
    success_url = reverse_lazy('index')
