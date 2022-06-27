from django.http import HttpResponseRedirect
from user_auth.models import Profile
from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate
from user_auth.forms import UserRegisterForm

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile/')
    return render(request, 'user_auth/index.html', {})


class UserLogIn(LoginView):
    template_name = 'user_auth/sing_up.html'


class UserLogOut(LogoutView):
    next_page = '/'


class UserRegister(View):

    def get(self, request):

        form = UserRegisterForm

        return render(request, 'user_auth/register.html', context={'form':form})

    def post(self, request):

        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            Profile.objects.create(
                user=user, 
                phone=phone, 
                email=email
            )
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/profile/')

        return render(request, 'user_auth/register.html', context={'form':form})

            
def profile(request):

    return render(request, 'user_auth/profile.html', {})

