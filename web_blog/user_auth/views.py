from django.http import HttpResponseRedirect
from user_auth.models import Profile
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate
from user_auth.forms import UserRegisterForm, UserEditProfileForm, UserEditForm
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

        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            avatar = request.FILES['avatar']
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
                email=email,
                avatar=avatar
            )
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/profile/')

        return render(request, 'user_auth/register.html', context={'form':form})

            
def profile(request):

    user = request.user
    #profile = Profile.objects.filter(user=user)
    posts = Blogs.objects.filter(user=user)
    user.profile.num_of_posts = posts.count()
    user.profile.save()

    return render(request, 'user_auth/profile.html', context={'posts':posts})

class UserProfileEdit(View):

    def get(self, request):

        user_form = UserEditForm(instance=request.user)
        profile_form = UserEditProfileForm(instance=request.user.profile)

        return render(request, 'user_auth/edit_profile.html', context={'user_form':user_form,
                                                                        'profile_form':profile_form})

    def post(self, request):

        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = UserEditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        
        if (user_form.is_valid() and profile_form.is_valid()):
            user_form.save()
            profile_form.save()
            
            return HttpResponseRedirect('/profile/')

        return render(request, 'user_auth/edit_profile.html', context={'user_form':user_form,
                                                                        'profile_form':profile_form})
            
            

