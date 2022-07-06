from django.contrib import admin
from blog_board.models import Blogs, Comments, ModerComment
from django.core.exceptions import PermissionDenied

class CommentsInlines(admin.TabularInline):
    model = Comments

class BlogsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'user', 'is_active']
    list_filter = ['created_at', 'is_active']
    inlines = [CommentsInlines]

    actions = ['activate', 'deactivate', 'set_unknown']

    def set_unknown(self, request, queryset):
        if not request.user.has_perm('blog_board.can_activate'):
            raise PermissionDenied('У вас нет прав для совершения этого действия')
        queryset.update(is_active=0)

    def activate(self, request, queryset):
        if not request.user.has_perm('blog_board.can_activate'):
            raise PermissionDenied('У вас нет прав для совершения этого действия')
        queryset.update(is_active=1)

    def deactivate(self, request, queryset):
        if not request.user.has_perm('blog_board.can_activate'):
            raise PermissionDenied('У вас нет прав для совершения этого действия')
        queryset.update(is_active=2)

    set_unknown.short_description = 'На рассмотрение'
    activate.short_description = 'Одобрить'
    deactivate.short_description = 'Запретить к публикации'

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'blog', 'ban_status']
    list_filter =  ['user', 'ban_status']

    actions = ['ban', 'unban']

    def ban(self, request, queryset):
        if not request.user.has_perm('blog_board.can_ban'):
            raise PermissionDenied('У вас нет прав для совершения этого действия')
        queryset.update(ban_status=True)
        
    def unban(self, request, queryset):
        if not request.user.has_perm('blog_board.can_ban'):
            raise PermissionDenied('У вас нет прав для совершения этого действия')
        queryset.update(ban_status=False)

    ban.short_description = 'Забанить комментарий'
    unban.short_description = 'Разбанить комметарий'

class ModerCommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'post']

admin.site.register(Blogs, BlogsAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(ModerComment, ModerCommentAdmin)