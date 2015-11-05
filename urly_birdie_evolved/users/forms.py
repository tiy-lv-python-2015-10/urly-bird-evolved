

from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    # email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
        widgets = {
             'password': forms.PasswordInput(attrs={'class': 'form-control'}),
             'username': forms.TextInput(attrs={'class': 'form-control'}),
             'email': forms.TextInput(attrs={'class': 'form-control'})
         }

    # def save(self, commit=True):
    #     user = super(RegistrationForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #
    #     if commit:
    #         user.save()
    #     return user

