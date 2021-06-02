from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields
from .models import Post


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    def clean(self):
        clean_data = super().clean()
        password = clean_data.get('password')
        password1 = clean_data.get('password1')

        if password != password1:
            raise ValidationError('Password does not match!!!')


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text', 'image']
