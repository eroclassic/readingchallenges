from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Challenge, User, Book, UserBook

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'goodreads_id', 'location')
    search_fields = ('username', 'email')

@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'created_at')
    search_fields = ('title', 'creator__username')