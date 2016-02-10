from django.contrib.auth.models import User
from django.db import models
from hashids import Hashids


class Bookmark(models.Model):
    """Bookmark stores url and creates 6 character hash e.g. 8x43SE"""
    human = models.ForeignKey(User, null=True, blank=True)
    title = models.CharField(max_length=60)
    url = models.URLField()
    description = models.TextField(max_length=700, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    @property
    def num_clicks(self):
        """
        :return: Number of times short url has been accessed
        """
        return self.click_set.all().count()

    @property
    def short_id(self):
        """
        :return: 6 charater hash using primary key as salt
        """
        hashids = Hashids(min_length=6)
        short = hashids.encode(self.id)
        return short

    @staticmethod
    def decode_id(code):
        """
        :param code: 6 character hash
        :return: int - to use for primary key
        """
        hashids = Hashids(min_length=6)
        decode = hashids.decode(code)
        return decode[0]

    def __str__(self):
        return self.title


class Click(models.Model):
    """Counts clicks of bookmarks"""
    human = models.ForeignKey(User, null=True, blank=True)
    bookmark = models.ForeignKey(Bookmark)
    clicked_at = models.DateTimeField(auto_now_add=True)