from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, CreateView
from users.forms import RegistrationForm


class Register(View):

 def get(self, request):
     form = RegistrationForm()
     return render(request, 'registration/register.html', {'form': form})

 def post(self, *args, **kwargs):
     form = RegistrationForm(self.request.POST)
     if form.is_valid():
         user = form.save(commit=False)
         user.user_name = form.cleaned_data['username']
         user.email = form.cleaned_data['email']
         user.set_password(form.cleaned_data['password'])
         user.save()
         return HttpResponseRedirect(reverse('bookmark_create'))

     return render(self.request, 'registration/register.html', {'form': form})


# class Register(CreateView):
#     model = User
#     form = UserCreationForm
#     fields = ('username', 'email', 'password')
#     template_name = 'registration/register.html'
#     success_url = reverse_lazy('login')

