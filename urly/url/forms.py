from django import forms
from django.forms import Textarea
from url.models import Url


class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ('title', 'message')
        widgets = {
            'message': Textarea(attrs={'rows': 2})
        }
