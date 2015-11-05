from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.views.generic import View, ListView, DetailView, CreateView
from bookmarks.models import Bookmark
from users.forms import UserCreateForm


class CreateUser(CreateView):

    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('list_bookmarks')
    template_name = 'users/register.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateUser, self).form_valid(form)






