from django.contrib import admin
from blog_board.models import Blogs, Comments

class CommentsInlines(admin.TabularInline):
    model = Comments

class BlogsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'user']
    list_filter = ['created_at']
    inlines = [CommentsInlines]

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'blog']

admin.site.register(Blogs, BlogsAdmin)
admin.site.register(Comments, CommentsAdmin)