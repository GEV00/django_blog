from django.db import models
from django.contrib.auth.models import User


class Blogs(models.Model):

    ACTIVITY_CHOISES = [
        (0, 'На рассмотрении'), #отобразить на странице профиля статус постов
        (1, 'Одобрено'),
        (2, 'Неодобрено (оставьте комментарий)') #рассмотреть возможность указания причины от модератора в  личном профиле
    ]

    title = models.CharField(max_length=15, verbose_name='Заголовок')
    text  = models.CharField(max_length=1000, verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                            related_name='blog_author', verbose_name='Пользователь')
    is_active = models.IntegerField(default=0, verbose_name='Одобрено модерацией',
                                    choices=ACTIVITY_CHOISES)

    class Meta:
        db_table = 'Блоги'          #название таблицы
        ordering = ['-created_at']   #сортировка по умолчанию по дате создания
        permissions = (
            ('can_activate', 'Can activate posts'),
        )

    def __str__(self):
        if len(self.text) > 100:
            return f"{self.text[:100]}..." #ограничение на отображение 100 символов при вызове объекта
        return self.text


class ModerComment(models.Model): # отработать удобную логику, сейчас совсем не удобно

    content = models.CharField(max_length=200, verbose_name='Комментарий от модератора')
    post = models.OneToOneField(Blogs, on_delete=models.CASCADE, null=True,
                                related_name='post', verbose_name='Неодобренная публикация')

    class Meta:
        db_table = 'Комментарий модератора'

    def __str__(self):
        return self.content
    

class BlogPhotos(models.Model):

    file = models.ImageField(upload_to='blog_photos/')

    post = models.ForeignKey(Blogs, on_delete=models.CASCADE, null=True,
                            verbose_name='Публикация', related_name='post1')

    class Meta:
        db_table = 'Фото публикаций'


class Comments(models.Model):

    DELETE_CHOISES = [
        (True, 'Удалено модератором'),
        (False, '')
    ]

    content = models.CharField(max_length=500, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                            related_name='comment_author', verbose_name='Пользователь')
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, null=True,
                            related_name='blog', verbose_name='Новость')
    ban_status = models.BooleanField(default=False, verbose_name='Статус',
                                choices=DELETE_CHOISES)

    class Meta:
        db_table = 'Комментарии'
        ordering = ['-created_at']

        permissions = (
            ('can_ban', 'Can ban comments'),
        )























