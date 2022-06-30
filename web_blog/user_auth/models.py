from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    VERIFY_CHOISES = [
        (True, 'Верифицирован'),
        (False, 'Неверифицирован')
    ]

    MODERATOR_CHOISES = [
        (True, 'Модератор'),
        (False, '')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='user', verbose_name='Пользователь')
    second_name = models.CharField(max_length=20, verbose_name='Фамилия')
    phone = models.CharField(max_length=11, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Почта')
    num_of_posts = models.IntegerField(default=0, verbose_name='Число постов')
    is_verify = models.BooleanField(default=False, verbose_name='Статус верификации',
                                    choices=VERIFY_CHOISES)
    is_moderator = models.BooleanField(default=False, verbose_name='Статус модерации',
                                    choices=MODERATOR_CHOISES)
    avatar = models.ImageField(upload_to='user_avatars/')

    class Meta:
        db_table = 'Профиль'
        permissions = (
            ('can_verify', 'Can verify users'),
            ('can_moderate', 'Can be a moderator'),
        )