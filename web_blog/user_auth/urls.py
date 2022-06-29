import profile
from unicodedata import name
from django.urls import path
from user_auth.views import *

urlpatterns = [
    path('', index, name='main_page'),
    path('singup/', UserLogIn.as_view(), name='sing_up'),
    path('singin/', UserRegister.as_view(), name='register'),
    path('logout/', UserLogOut.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', UserProfileEdit.as_view(), name='profile_edit'),
]
