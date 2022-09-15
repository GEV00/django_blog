import re
from urllib import response
from django.test import TestCase
from .models import Blogs, Comments
from django.contrib.auth.models import User
from django.urls import reverse


NUM_OF_BLOGS = 10

NUM_OF_COMMENTS = 3

USERNAME = 'authenticated_user'

#USER_PASSWORD = 'authenticated_user_password'

#Create your tests here.
class TestBlogs(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        '''Создадим пользователя и его 10 новостей'''

        user = User.objects.create(
            username=USERNAME,
        )

        for i in range(NUM_OF_BLOGS):
            Blogs.objects.create(
                title=f"blog {i}",
                text='sometext',
                user=user,
                is_active=1
            )

    def test_blog_list_exist_on_right_url_and_template(self):
        response = self.client.get('/blogs/')
        self.assertEqual(response.status_code, 200) # проверяем, если ли страница по url
        self.assertTemplateUsed(response, 'blog_board/listblog_view.html') # тот ли шаблон используется
        
    def test_blog_create_creates_not_active_blog(self):
        self.client.force_login(User.objects.get(username=USERNAME)) # имитируем залогированного пользователя, который будет в запросе
        response = self.client.post(
            reverse('blog_creation'),
            {'title':'test_blog', 'text':'some_text'}, 
            ) # post запрос с заполненной формой. В качестве request.user передается созданный выше пользователь

        blog = Blogs.objects.get(title='test_blog') # забираем из БД созданную в представлении запись 
        self.assertEqual(response.status_code, 302) # проверяем ответ страницы 
        self.assertEqual(blog.is_active, 0) # проверяем, что созданная запись не будет опубликована сразу же после создания

# class TestComments(TestCase):
    
#     @classmethod
#     def setUpTestData(cls) -> None:
#         '''Создадим пользователя и новость'''

#         user = User.objects.create(
#             username=USERNAME,
#         )

#         blog = Blogs.objects.create(
#                 title="blog",
#                 text='sometext',
#                 user=user,
#             )