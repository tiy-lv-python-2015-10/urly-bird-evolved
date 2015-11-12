from django.contrib.auth.models import User
from django.db import models
from hashids import Hashids


class Bookmark(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    link = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True, blank=True)

    @property
    def short_link(self):
        hashids = Hashids(min_length=6)
        hash_link = hashids.encode(self.id)
        return hash_link

    @staticmethod
    def decode(hash_link):
        hashids = Hashids(min_length=6)
        link = hashids.decode(hash_link)
        return link[0]


class Click(models.Model):
    user = models.OneToOneField(User)
    bookmark = models.ForeignKey(Bookmark)
    timestamp = models.DateTimeField(auto_now_add=True)

