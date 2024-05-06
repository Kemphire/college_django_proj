from django.apps import AppConfig

class UserAuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_authentication'
    # before overriding this method the profile was not properly initiated by default
    def ready(self):
        import user_authentication.signals
