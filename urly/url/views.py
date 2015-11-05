from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.utils import timezone
from django.views.generic import View, ListView, DetailView, CreateView
from url.forms import ChirpForm
from url.models import url


class ListUrls(ListView):
    model = Url
    queryset = Url.objects.order_by('-posted_at')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_load'] = timezone.now()
        return context


class UrlDetail(DetailView):
    model = Url

class CreateUrl(CreateView):
    model = Url
    form_class = UrlForm
    success_url = reverse_lazy('list_urls')
    template_name = 'url/url_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateUrl, self).form_valid(form)

