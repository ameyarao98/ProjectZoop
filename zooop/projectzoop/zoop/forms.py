from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from zoop.models import Post

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs={'class':'form-group form-control',
        'placeholder':'Username', 'autofocus':''}
        self.fields['email'].widget.attrs={'class':'form-group form-control',
        'placeholder':'Email', 'autofocus':''}
        self.fields['password1'].widget.attrs={'class':'form-group form-control',
        'placeholder':'Password', 'value':''}
        self.fields['password2'].widget.attrs={'class':'form-group form-control',
        'placeholder':'Confirm Password', 'value':''}
        self.fields['username'].label = False
        self.fields['username'].help_text = ""
        self.fields['email'].label = False
        self.fields['password1'].label = False
        self.fields['password2'].label = False


    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    user = forms.CharField(required=True, label=False)
    password = forms.CharField(widget=forms.PasswordInput(), label=False)

    class Meta:
        model = User
        fields = ("user", "password")

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget.attrs={'class':'form-group form-control',
        'placeholder':'Username', 'autofocus':''}
        self.fields['password'].widget.attrs={'class':'form-group form-control',
        'placeholder':'Password', 'value':''}

class AddPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddPostForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = 'Zoop what\'s on your mind'

    class Meta:
        model = Post
        fields = ['content']

        widgets = {
            'content' : forms.Textarea(attrs={'class':'form-control', 'rows' : 3, 'style':'resize:none;'}),
        }
