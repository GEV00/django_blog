from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=True, help_text='Имя')
    second_name = forms.CharField(max_length=20, required=True, help_text='Фамилия')
    last_name = forms.CharField(max_length=20, required=False, help_text='Отчество')
    phone = forms.CharField(max_length=11, help_text='Номер телефона')
    email = forms.EmailField(help_text='Почта')
    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'avatar','first_name', 'second_name', 'last_name',
                'phone', 'email', 'password1', 'password2',)


class UserEditProfileForm(UserChangeForm):

    second_name = forms.CharField(max_length=20, required=True, help_text='Фамилия')
    phone = forms.CharField(max_length=11, help_text='Номер телефона')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'second_name', 'last_name',
                'phone', 'email',)