"""URLy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from bookmark.views import CreateBookmark, BookmarkDetail
from users.views import CreateUser, ListBookmark, ListProfile, BookmarkDelete, BookmarkUpdate

urlpatterns = [
    url(r'$^', ListBookmark.as_view(), name='list_bookmarks'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/register/', CreateUser.as_view(), name='register'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^accounts/profile', login_required(ListProfile.as_view()), name='list_profile'),
    url(r'^create/$', login_required(CreateBookmark.as_view()), name='bookmark_create'),
    url(r'(?P<pk>\d+)/$', BookmarkDetail.as_view(), name='bookmark_detail'),
    url(r'(?P<short_link>\w+)/$', 'bookmark.views.link', name='link'),
    url(r'delete/(?P<pk>\d+)', BookmarkDelete.as_view(), name='delete_bookmark'),
    url(r'edit/(?P<pk>\d+)', BookmarkUpdate.as_view(), name='update_bookmark')

]
