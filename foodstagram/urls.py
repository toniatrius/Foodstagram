from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("foodstagram.common.urls")),
    path("accounts/", include("foodstagram.accounts.urls")),
    path("recipes/", include("foodstagram.recipes.urls")),
]

handler404 = "foodstagram.common.views.error_404_view"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
