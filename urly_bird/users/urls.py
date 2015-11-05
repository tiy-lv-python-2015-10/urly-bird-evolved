from django.conf.urls import url, include, patterns
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^login/register/', views.CreateUser),

]
