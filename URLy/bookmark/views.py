from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DetailView
from bookmark import models
from bookmark.forms import BookmarkForm
from bookmark.models import Bookmark


class CreateBookmark(CreateView):
    model = Bookmark
    form_class = BookmarkForm
    success_url = reverse_lazy('list_profile')
    template_name = 'bookmark/bookmark_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateBookmark, self).form_valid(form)


class BookmarkDetail(DetailView):
    model = Bookmark


def link(request, short_link):
    bookmark_id = models.Bookmark.decode(short_link)
    site = get_object_or_404(models.Bookmark, id=bookmark_id)
    models.Bookmark.objects.filter(id=bookmark_id)
    return redirect(site.link)
