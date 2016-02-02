from django.conf.urls import include, url
from users.views import Register

urlpatterns = [
    url(r'^register/$', Register.as_view() , {'next_page': '/login/'}, name='register')
]