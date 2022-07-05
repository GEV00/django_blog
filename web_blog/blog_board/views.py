from asyncio.windows_events import NULL
import csv
from wsgiref.util import request_uri
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from blog_board.models import Blogs, Comments, ModerComment, BlogPhotos
from blog_board.forms import BlogForm, CommentForm, CSVForm

class BlogListView(ListView):
    model = Blogs
    context_object_name = 'blog_list'
    template_name = 'blog_board/listblog_view.html'


def detail_blog(request, blog_id):
    
    blog_data = BlogPhotos.objects.filter(post_id=blog_id)
    comments = Comments.objects.filter(blog_id=blog_id)
    if (blog_data[0].post.is_active == 2):
        moder_comm = ModerComment.objects.filter(post=blog_data[0].post)
    else:
        moder_comm = NULL

    return render(request, 'blog_board/blog_view.html', context={'blog_data':blog_data,
                                                                'comments':comments,
                                                                'moder_comm':moder_comm})


class CreateBlogView(View):
    
    def get(self, request):

        form = BlogForm

        return render(request, 'blog_board/create_blog.html', context={'form':form})

    def post(self, request):
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            #form.cleaned_data['user'] = request.user
            blog = Blogs.objects.create(**{
                'title':form.cleaned_data['title'],
                'text':form.cleaned_data['text'],
                'user':request.user
            })
            files = request.FILES.getlist('images')
            for f in files:
                BlogPhotos.objects.create(**{
                    'file':f,
                    'post':blog
                })
            return HttpResponseRedirect('../')
        return render(request, 'blog_board/create_blog.html', context={'form':form})


class CreateBlogFromCSV(View):
    
    def get(self, request):

        form = CSVForm

        return render(request, 'blog_board/csv_loading.html', context={'form':form})

    def post(self, request):
        
        form = CSVForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES('file')
            with open(file, newline='') as f:
                blogs_data = csv.reader(f)
                for raw in blogs_data:
                    #валидация файла см. в forms.py
                    title = raw[0]
                    text = raw[1]
                    Blogs.objects.create(**{
                        'title':title,
                        'text':text,
                        'user':request.user
                    })
            return HttpResponseRedirect('../../')

        return render(request, 'blog_board/csv_loading.html', context={'form':form})

class CreateCommentView(View):
    
    def get(self, request, blog_id):

        form = CommentForm

        return render(request, 'blog_board/create_comment.html', context={'form':form})

    def post(self, request, blog_id):

        form = CommentForm(request.POST)

        if form.is_valid():
            form.cleaned_data['user'] = request.user
            form.cleaned_data['blog_id'] = blog_id
            Comments.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('../')

        return render(request, 'blog_board/create_comment.html', context={'form':form})


class EditCommentView(View):

    def get(self, request, blog_id, comm_id):

        comment = Comments.objects.get(id=comm_id)
        form = CommentForm(instance=comment)

        return render(request, 'blog_board/edit_comment.html', context={'form':form})

    def post(self, request, blog_id, comm_id):#blog_id необходимо указать для работы ссылки редиректа

        form = CommentForm(request.POST)

        if form.is_valid():
            Comments.objects.filter(id=comm_id).update(content=form.cleaned_data['content'])
            return HttpResponseRedirect('../../') #редирект обратно к новости

        return render(request, 'blog_board/edit_comment.html', context={'form':form})
