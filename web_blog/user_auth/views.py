from django.http import HttpResponseRedirect
from user_auth.models import Profile
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate
from user_auth.forms import UserRegisterForm, UserEditProfileForm
from blog_board.models import Blogs

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
            second_name = form.cleaned_data['second_name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            Profile.objects.create(
                user=user,
                second_name=second_name, 
                phone=phone, 
                email=email
            )
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/profile/')

        return render(request, 'user_auth/register.html', context={'form':form})

            
def profile(request):

    profile = Profile.objects.filter(user=request.user)
    posts = Blogs.objects.filter(user=request.user)
    profile.update(num_of_posts=posts.count())

    return render(request, 'user_auth/profile.html', context={'profile':profile[0],
                                                                'posts':posts})

class UserProfileEdit(View):

    def get(self, request):

        user = request.user
        form = UserEditProfileForm(instance=user)

        return render(request, 'user_auth/edit_profile.html', context={'form':form})

    def post(self, request):

        user = request.user
        username = user.username
        form = UserEditProfileForm(request.POST, instance=user)

        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            second_name = form.cleaned_data['second_name']
            phone = form.cleaned_data['phone']
            User.objects.filter(username=username).update(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            Profile.objects.filter(user=user).update(
                second_name=second_name,
                phone=phone
            )
            return HttpResponseRedirect('/profile/')

        return render(request, 'user_auth/edit_profile.html', context={'form':form})
            
            

