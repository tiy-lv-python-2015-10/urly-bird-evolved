from django.contrib import admin
from url.models import Url, Tag


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ('author', 'message', 'posted_at')
    list_filter = ('author', 'posted_at')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'posted_at')