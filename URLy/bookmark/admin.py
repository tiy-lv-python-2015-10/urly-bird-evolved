from django.contrib import admin
from .models import *

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'description', 'link', 'timestamp', 'modified', 'short_link')


@admin.register(Click)
class Click(admin.ModelAdmin):
    list_display = ('user', 'bookmark', 'timestamp')