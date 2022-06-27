from django.db import models
from django.contrib.auth.models import User


class Blogs(models.Model):
    title = models.CharField(max_length=15, verbose_name='Заголовок')
    text  = models.CharField(max_length=1000, verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                            related_name='blog_author', verbose_name='Пользователь')

    class Meta:
        db_table = 'Блоги'          #название таблицы
        ordering = ['-created_at']   #сортировка по умолчанию по дате создания

    def __str__(self):
        if len(self.text) > 100:
            return f"{self.text[:100]}..." #ограничение на отображение 100 символов при вызове объекта
        return self.text

class Comments(models.Model):
    content = models.CharField(max_length=500, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                            related_name='comment_author', verbose_name='Пользователь')
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, null=True,
                            related_name='blog', verbose_name='Новость')

    class Meta:
        db_table = 'Комментарии'
        ordering = ['-created_at']