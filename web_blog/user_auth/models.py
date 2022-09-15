from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Profiles(models.Model):

    VERIFY_CHOISES = [
        (True, _('Verify')),
        (False, _('Not verify'))
    ]

    MODERATOR_CHOISES = [
        (True, _('Moderator')),
        (False, '')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile', verbose_name=_('User'))
    second_name = models.CharField(max_length=20, verbose_name=_('Last Name'))
    phone = models.CharField(max_length=11, verbose_name=_('Phone Number'))
    #email = models.EmailField(verbose_name='Почта')
    num_of_posts = models.IntegerField(default=0, verbose_name=_('Number of posts'))
    is_verify = models.BooleanField(default=False, verbose_name=_('Verify status'),
                                    choices=VERIFY_CHOISES)
    is_moderator = models.BooleanField(default=False, verbose_name=_('Moderator status'),
                                    choices=MODERATOR_CHOISES)
    avatar = models.ImageField(upload_to='user_avatars/')

    class Meta:
        db_table = 'Профиль'

        permissions = (
            ('can_verify', 'Can verify users'),
            ('can_moderate', 'Can be a moderator'),
        )
        verbose_name_plural = _('profiles')
        verbose_name = _('profile')