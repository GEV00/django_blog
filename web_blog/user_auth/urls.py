import profile
from django.urls import path
from user_auth.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', index, name='main_page'),
    path('singup/', UserLogIn.as_view(), name='sing_up'),
    path('singin/', UserRegister.as_view(), name='register'),
    path('logout/', UserLogOut.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', UserProfileEdit.as_view(), name='profile_edit'),
]+ static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

#конструкция +static... помогает корректно обрабатывать ссылки на файлы