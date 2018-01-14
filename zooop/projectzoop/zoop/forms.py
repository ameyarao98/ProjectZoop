from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
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

class LoginForm(AuthenticationForm):
    username = forms.CharField( label=False)
    password = forms.CharField(widget=forms.PasswordInput, label=False)

    error_messages = {
        'invalid_login': ("Please enter a correct %(username)s and password. "
                           "Note that both fields may be case-sensitive."),
        'inactive': ("This account is inactive."),
    }

    class Meta:
        model = User
        fields = ("username", "password")

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs={'class':'form-group form-control',
        'placeholder':'Username', 'autofocus':''}
        self.fields['password'].widget.attrs={'class':'form-group form-control',
        'placeholder':'Password', 'value':''}

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

class AddPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddPostForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = 'Zoop what\'s on your mind'

    class Meta:
        model = Post
        fields = ['content']

        widgets = {
            'content' : forms.Textarea(attrs={'id': 'emoji-form', 'class':'form-control', 'rows' : 3, 'style':'resize:none;display: none'}),
        }
