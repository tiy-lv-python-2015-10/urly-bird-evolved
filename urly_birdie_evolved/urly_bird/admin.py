from django.contrib import admin
from urly_bird.models import Bookmark, Click


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'human', 'title', 'url', 'description', 'created_at')


@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    list_display = ('id', 'human', 'bookmark', 'clicked_at')
