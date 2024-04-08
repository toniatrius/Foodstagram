from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "foodstagram.accounts"

    def ready(self):
        import foodstagram.accounts.signals
