from django.conf.urls import url, include, patterns
from django.contrib.auth import views as auth_views

from . import views
from bookmarks.views import ListBookMarks
from django.conf.urls import (
handler400, handler403, handler404, handler500
)

urlpatterns = [
    url(r'^bookmarks/', ListBookMarks.as_view(), name="list_bookmarks"),


]




