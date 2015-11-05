from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from url.views import ListUrls, UrlDetail, CreateUrl

# Note that the as_view() has to be called to convert a CBV to a normal view
urlpatterns = [
    url(r'^$', ListUrls.as_view(), name='list_urls'),
    url(r'^(?P<pk>\d+)/$', UrlDetail.as_view(),
        name='url_detail'),
    url(r'^create/$', login_required(CreateUrl.as_view()), name='url_create'),
]
