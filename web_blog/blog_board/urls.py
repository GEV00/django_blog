from django.urls import path
from blog_board.views import *

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<int:blog_id>/', detail_blog, name='blog_view'),
    path('create/', CreateBlogView.as_view(), name='blog_creation'),
    path('<int:blog_id>/add_com/', CreateCommentView.as_view(), name='comment_creation'),
    path('<int:blog_id>/edit_com/<int:comm_id>/', EditCommentView.as_view(), name='edit_comment'),
]