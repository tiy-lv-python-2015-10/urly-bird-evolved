from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, DeleteView, UpdateView
from bookmark.forms import BookmarkForm
from bookmark.models import Bookmark
from users.forms import RegistrationForm


class CreateUser(CreateView):
    model = User
    form_class = RegistrationForm
    success_url = reverse_lazy('list_profile')
    template_name = 'users/register.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateUser, self).form_valid(form)


class ListBookmark(ListView):
    model = Bookmark
    queryset = Bookmark.objects.order_by('-timestamp')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_load'] = timezone.now()
        return context


class ListProfile(ListView):
    model = Bookmark
    template_name = 'bookmark/profile_list.html'
    paginate_by = 5

    def get_queryset(self):
        return Bookmark.objects.filter(user__username=self.request.user.username).order_by('-timestamp')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_load'] = timezone.now()
        return context


class BookmarkUpdate(UpdateView):
    model = Bookmark
    form_class = BookmarkForm
    template_name_suffix = '_update_form'


class BookmarkDelete(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list_profile')


