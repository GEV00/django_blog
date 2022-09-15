from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User


class Blogs(models.Model):

    ACTIVITY_CHOISES = [
        (0, _('On cheak')), #отобразить на странице профиля статус постов
        (1, _('Approved')),
        (2, _('Not approved (leave your comment)')) #рассмотреть возможность указания причины от модератора в  личном профиле
    ]

    title = models.CharField(max_length=15, verbose_name=_('Title'))
    text  = models.CharField(max_length=1000, verbose_name=_('Content'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created_at'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                            related_name='blog_author', verbose_name=_('User'))
    is_active = models.IntegerField(default=0, verbose_name=_('Approve by moderator'),
                                    choices=ACTIVITY_CHOISES)

    def __str__(self):
        if len(self.text) > 100:
            return f"{self.text[:100]}..." #ограничение на отображение 100 символов при вызове объекта
        return self.text

    class Meta:
        db_table = 'Блоги'          #название таблицы
        ordering = ['-created_at']   #сортировка по умолчанию по дате создания
        permissions = (
            ('can_activate', 'Can activate posts'),
        )
        verbose_name_plural = _('blogs') # для интернационализации модели
        verbose_name = _('blog')


class ModerComment(models.Model): # отработать удобную логику, сейчас совсем не удобно

    content = models.CharField(max_length=200, verbose_name=_('Comment from moderator'))
    post = models.OneToOneField(Blogs, on_delete=models.CASCADE, null=True,
                                related_name='post', verbose_name=_('Not approved post'))

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'Комментарий модератора'
        verbose_name_plural = _('moder_comments') # для интернационализации модели
        verbose_name = _('moder_comment')
    

class BlogPhotos(models.Model):

    file = models.ImageField(upload_to='blog_photos/')

    post = models.ForeignKey(Blogs, on_delete=models.CASCADE, null=True,
                            verbose_name=_('Post'), related_name='post1')

    class Meta:
        db_table = 'Фото публикаций'
        verbose_name_plural = _('blog_photos') # для интернационализации модели
        verbose_name = _('blog_photo')

class Comments(models.Model):

    DELETE_CHOISES = [
        (True, 'Удалено модератором'),
        (False, '')
    ]

    content = models.CharField(max_length=500, verbose_name=_('Comment'))
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                            related_name='comment_author', verbose_name=_('User'))
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, null=True,
                            related_name='blog', verbose_name=_('Blog'))
    ban_status = models.BooleanField(default=False, verbose_name=_('Status'),
                                choices=DELETE_CHOISES)

    class Meta:
        db_table = 'Комментарии'
        ordering = ['-created_at']

        permissions = (
            ('can_ban', 'Can ban comments'),
        )
        verbose_name_plural = _('comments') # для интернационализации модели
        verbose_name = _('comment')























