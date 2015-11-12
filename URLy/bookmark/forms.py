from django.forms import Textarea, URLInput
from django.forms.models import ModelForm
from bookmark.models import Bookmark


class BookmarkForm(ModelForm):
    class Meta:
        model = Bookmark
        fields = ('title', 'description', 'link')
        widgets = {
            'message': Textarea(attrs={'rows': 2}),
            'link': URLInput()
        }
