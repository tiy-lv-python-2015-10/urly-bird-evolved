from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from urly_bird.views import ListBookmarks, CreateBookmark, BookmarkDetail, UpdateBookmark, DeleteBookmark, \
    ListUserBookmarks

urlpatterns = [
    url(r'^$', ListBookmarks.as_view(), name='list_bookmarks'),
    url(r'^create/$', login_required(CreateBookmark.as_view()), name='bookmark_create'),
    url(r'^update/(?P<pk>\d+)/$', UpdateBookmark.as_view(), name='bookmark_update'),
    url(r'^delete/(?P<pk>\d+)/', DeleteBookmark.as_view(), name='bookmark_delete'),
    url(r'^(?P<pk>\d+)/$', BookmarkDetail.as_view(), name='bookmark_detail'),
    url(r'^me/$', ListUserBookmarks.as_view(), name='user_list'),
    url(r'^(?P<user_name>.*)/$', 'urly_bird.views.user_list', name='any_list')
]
