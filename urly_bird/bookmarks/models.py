import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from users.models import Profile

class Bookmark(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    bookmark_url = models.URLField(null=True, blank=True)
    bookmark_hash = models.CharField(max_length=6, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True, blank=True)



class Click(models.Model):
    bookmark = models.ForeignKey(Bookmark)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User ,null=True, blank=True)
