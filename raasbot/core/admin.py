from django.contrib import admin
from .models import (
    User,
    Bot,
    UserMessageData,
    ScrapedUser,
    Message,
    Text,
    RestrictedRoles,
    LogData
)
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    list_display = ['user', 'token', 'is_alive']
    list_filter = ['user', 'is_alive']
    search_fields = ['token']
    list_editable = ['is_alive']


@admin.register(UserMessageData)
class UserMessageDataAdmin(admin.ModelAdmin):
    list_filter = ['user']

@admin.register(ScrapedUser)
class ScrapedUserAdmin(admin.ModelAdmin):
    list_filter = ['texted', 'user']
    search_fields = ['name']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_filter = ['user']

@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_filter = ['user']

@admin.register(RestrictedRoles)
class RoleAdmin(admin.ModelAdmin):
    list_filter = ['user']

@admin.register(LogData)
class LogDataAdmin(admin.ModelAdmin):
    list_filter = ['success', 'user']
