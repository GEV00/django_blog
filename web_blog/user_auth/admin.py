from django.contrib import admin
from user_auth.models import Profile
from django.core.exceptions import PermissionDenied


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_verify', 'is_moderator']
    actions = ['set_verify', 'set_unverify', 'set_moder', 'set_unmod']
    list_filter = ['user', 'is_verify']
    search_fields = ['user']

    fieldsets = (
        ('Основные сведения', {
            "fields": (
                'user', 'second_name', 'avatar'
            ),
        }),
        ('Контактные данные', {
            "fields": (
                'phone', 'email'
            ),
        }),
        ('Дополнительная информация', {
            "fields": (
                'num_of_posts', 'is_verify', 'is_moderator'
            ),
        }),
    )
    

    def set_verify(self, request, queryset):
        # при проверке permissions, добавляемого в Meta модели не нужно указывать ..._<model>:
        # просто <app>.<action> 
        if not request.user.has_perm('user_auth.can_verify'):
            raise PermissionDenied('У вас нет разрешения к этому действию')
        queryset.update(is_verify=True)
        for profile in queryset:
            profile.user.groups.add(3)#become verify user

    def set_unverify(self, request, queryset):
        if not request.user.has_perm('user_auth.can_verify'):
            raise PermissionDenied('У вас нет разрешения к этому действию')
        queryset.update(is_verify=False)
        for profile in queryset:
            profile.user.groups.remove(3)

    def set_moder(self, request, queryset):
        if not request.user.has_perm('user_auth.can_moderate'):
            raise PermissionDenied('У вас нет разрешения к этому действию')
        queryset.update(is_moderator=True)
        queryset.update(is_verify=True)
        for profile in queryset:
            profile.user.is_staff = True #!!!!DOES NOT WORK CORRECTLY (WHYYYY)!!!!!!
            profile.user.groups.add(2) #become moderator
            profile.user.groups.add(3) # if u are a moder then u are vefify
            print(profile.user.is_staff)
    
    def set_unmod(self, request, queryset):
        if not request.user.has_perm('user_auth.can_moderate'):
            raise PermissionDenied('У вас нет разрешения к этому действию')
        queryset.update(is_moderator=False)
        for profile in queryset:
            profile.user.is_staff = False #!!!!DOES NOT WORK CORRECTLY (WHYYYY)!!!!!!
            profile.user.groups.remove(2) #stop being a moderator but u still verify

    set_verify.short_description = 'Верифицировать'
    set_unverify.short_description = 'Снять верификацию'
    set_moder.short_description = 'Сделать модератором'
    set_unmod.short_description = 'Снять статус модератора'

admin.site.register(Profile, ProfileAdmin)
