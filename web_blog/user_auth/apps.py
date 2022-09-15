from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UserAuthConfig(AppConfig):
    name = 'user_auth'
    verbose_name = _('profiles') # для интернационализации упаковываем в gettext 
