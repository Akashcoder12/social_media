from django import forms
from .models import Post,Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UsernameChangeForm(forms.ModelForm):
  class Meta:
    model=User
    fields=['username']
    
class PostForm(forms.ModelForm):
   class Meta:
     model=Post
     fields=['content','image']
     
     
class CommentForm(forms.ModelForm):
   class Meta:
     model=Comment
     fields=['content']
     
     
     


class CustomSignupForm(UserCreationForm):
    date_of_birth = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    address = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'rows': 3})
    )
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "date_of_birth", "address", "profile_picture"]
