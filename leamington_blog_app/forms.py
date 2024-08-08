from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError 
from .models import Post, Comment, Profile


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Please enter a valid email address.',
                             widget=forms.EmailInput(attrs={'autocomplete': 'off'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'slug', 'tags']
        widgets = {
            'tags': forms.TextInput(attrs={'placeholder': 'Add tags, separated by commas'}),
        }

    def clean_slug(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise ValidationError("Title must be provided to generate a slug.")
        
        slug = self.cleaned_data.get('slug')
        if not slug:
            slug = slugify(title)
        
        return slug

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PostForm, self).__init__(*args, **kwargs)     
        

        if user and not user.is_staff:
            # remove fields for non-staff users
            self.fields.pop('slug', None)
            self.fields.pop('status', None)
            

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['bio']