from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return "username: {}".format(self.user.username)
