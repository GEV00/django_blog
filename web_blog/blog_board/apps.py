from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BlogBoardConfig(AppConfig):
    name = 'blog_board'
    verbose_name = _('blogs')
