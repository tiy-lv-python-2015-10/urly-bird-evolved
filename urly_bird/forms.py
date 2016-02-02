from django import forms
from urly_bird.models import Bookmark
from django.forms import Textarea


class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ('url', 'title', 'description')
        widgets = {
            'description': Textarea(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'})
        }

class CreateB(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ('url', 'title')