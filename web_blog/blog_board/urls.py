from django.urls import path
from blog_board.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<int:blog_id>/', detail_blog, name='blog_view'),
    path('create/', CreateBlogView.as_view(), name='blog_creation'),
    path('create/from_csv/', CreateBlogFromCSV.as_view(), name='blog_csv_creation'),
    path('<int:blog_id>/add_com/', CreateCommentView.as_view(), name='comment_creation'),
    path('<int:blog_id>/edit_com/<int:comm_id>/', EditCommentView.as_view(), name='edit_comment'),
]+ static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

#конструкция +static... помогает корректно обрабатывать ссылки на файлы