from django.contrib import admin
from .models import Bookmark, Click

# Register your models here.
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id','title','description','bookmark_url', 'timestamp', 'user')


@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    list_display = ('bookmark','timestamp', 'user')