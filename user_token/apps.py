from django.apps import AppConfig


class UserTokenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_token'

    def ready(self) -> None:
        import user_token.signals