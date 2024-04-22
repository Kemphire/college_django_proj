from django.apps import AppConfig

class UserAuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_authentication'

    def read(self):
        import user_authentication.signals
