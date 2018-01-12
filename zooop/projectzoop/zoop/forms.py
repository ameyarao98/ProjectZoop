from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from zoop.models import Post

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
