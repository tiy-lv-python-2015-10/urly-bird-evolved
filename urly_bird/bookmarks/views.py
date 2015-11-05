from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from hashids import Hashids
from bookmarks.models import Bookmark
from bookmarks.forms import BookmarkForm
from django.views.generic import TemplateView
from django.shortcuts import render_to_response

# Create your views here.
class ListBookMarks(ListView):
    model = Bookmark
    queryset = Bookmark.objects.order_by('-timestamp')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_load'] = timezone.now()
        return context


class ListProfile(ListView):
   model = Bookmark
   template_name = 'bookmarks/profile_list.html'
   paginate_by = 5

   def get_queryset(self):
       return Bookmark.objects.filter(user__username=self.request.user.username).order_by('-timestamp')

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['page_load'] = timezone.now()
       return context

class BookmarkDetail(DetailView):
    model = Bookmark


class EditBookmark(UpdateView):
    model = Bookmark
    form_class = BookmarkForm
    success_url = reverse_lazy('list_bookmarks')
    template_name_suffix = '_update_form'


class DeleteBookmark(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list_bookmarks')





class CreateBookmark(CreateView):
    model = Bookmark
    form_class = BookmarkForm
    success_url = reverse_lazy('list_bookmarks')
    template_name = 'bookmarks/bookmark_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        hashids = Hashids(salt='this is my salt 2',min_length=6)
        hashid = hashids.encode(4343984394839483989489849389483)

        return super(CreateBookmark, self).form_valid(form)

def welcome_page(request):
   return render_to_response('bookmarks/welcome_page.html')





from django.contrib.auth import logout

def logout_view(request):
    logout(request)



from django.shortcuts import render_to_response
from django.template import RequestContext


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response







