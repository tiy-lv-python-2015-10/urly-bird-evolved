from django.core.urlresolvers import reverse_lazy, reverse
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils import timezone
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from urly_bird.forms import BookmarkForm, CreateB
from urly_bird.models import Bookmark, Click


class ListBookmarks(ListView):
    """ List of all Bookmarks ordered by the most popular """
    model = Bookmark
    queryset = Bookmark.objects.annotate(num=Count('click__bookmark')).order_by('-num')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_load'] = timezone.now()
        return context


class ListUserBookmarks(ListView):
    """ List of bookmarks only for the logged in user. Template allows update and delete"""
    model = Bookmark
    template_name = 'urly_bird/bookmark_user_list.html'
    paginate_by = 5

    def get_queryset(self):
        return Bookmark.objects.filter(human__username=self.request.user.username).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_load'] = timezone.now()
        return context


class CreateBookmark(CreateView):
    """Create bookmark form accessed by logged in users only"""
    model = Bookmark
    form_class = BookmarkForm
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):
        """Assign created bookmark logged in user"""
        form.instance.human = self.request.user
        return super(CreateBookmark, self).form_valid(form)


class BookmarkDetail(DetailView):
    model = Bookmark


class UpdateBookmark(UpdateView):
    """Update bookmark form"""
    model = Bookmark
    form_class = BookmarkForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('list_bookmarks')

    def form_valid(self, form):
        form.instance.human = self.request.user
        return super(UpdateBookmark, self).form_valid(form)


class DeleteBookmark(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list_bookmarks')


def link(request, link_id):
    """
    Convert a hash into a primary key of a bookmark. Redirect to url of that bookmark.
    :param request:
    :param link_id: hash
    :return: redirect to bookmark.url
    """
    bkmrk_id = Bookmark.decode_id(link_id)
    bookmark = get_object_or_404(Bookmark, pk=bkmrk_id)
    if request.user.is_authenticated():
        Click.objects.create(human=request.user, bookmark=bookmark)
    else:
        Click.objects.create(bookmark=bookmark)
    return redirect(bookmark.url)


def user_list(request, user_name):
    """
    Display list of bookmarks for any given user
    :param request:
    :param user_name: username of user
    :return: render template for any user list
    """
    bookmarks = get_list_or_404(Bookmark.objects.all().filter(human__username=user_name))
    return render(request, 'urly_bird/any_user_list.html', {'bookmarks': bookmarks})

""" KEPT FOR QUESTIONS
class AnyUserBookmarks(ListView):
    model = Bookmark
    template_name = 'urly_bird/zzzzz.html'

    def dispatch(self, request, *args, **kwargs):
        thing = args

    def get_queryset(self):
        return Bookmark.objects.filter(human__username=thing)
"""

# def creatething(request):
#     if request.method == 'POST':
#         form = CreateB(request.POST)
#
#         if form.is_valid():
#             bookmark = form.save(commit=False)
#             bookmark.human = request.user
#             bookmark.save()
#
#             return HttpResponseRedirect(reverse('list_bookmarks'))
#         else:
#             HttpResponseRedirect(reverse('bookmark_create'))
#
#     return(render, 'urly_bird/bookmark_list.html', {'form': form})