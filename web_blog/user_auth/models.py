from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='user', verbose_name='Пользователь')
    phone = models.CharField(max_length=11, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Почта')
    num_of_posts = models.IntegerField(default=0, verbose_name='Число постов')

    class Meta:
        db_table = 'Профиль'
