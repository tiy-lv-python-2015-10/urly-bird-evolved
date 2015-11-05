"""urly_bird URL Configuration

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
from bookmarks.views import ListBookMarks, ListProfile, DeleteBookmark, EditBookmark
from users.views import CreateUser
from bookmarks.views import CreateBookmark, BookmarkDetail
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView



urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="bookmarks/welcome_page.html"), name='welcome_page'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': "/"}, name='logout'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^register/', CreateUser.as_view(), name='register'),
    url(r'^bookmarks/$', ListBookMarks.as_view(), name="list_bookmarks"),
    url(r'^my_bookmarks/$', ListProfile.as_view(), name="list_profile"),
    url(r'^create/$', login_required(CreateBookmark.as_view()), name='chirp_create'),
    url(r'^bookmarks/(?P<pk>\d+)/$', BookmarkDetail.as_view(),name='bookmark_detail'),
    url(r'^update/(?P<pk>\d+)', EditBookmark.as_view(), name='bookmark_edit'),
    url(r'^delete/(?P<pk>\d+)', DeleteBookmark.as_view(), name='bookmark_delete'),


]
