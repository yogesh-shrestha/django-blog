from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.conf import settings
from django import forms
from .models import User
from blog.models import Profile


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'




class UserSettingForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UserSettingForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'



class PasswordResetForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'




class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_image', 'facebook_url', 'twiiter_url', 'instagram_url', 'linkedin_url', 'pinterest_url']


        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twiiter_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.TextInput(attrs={'class': 'form-control'}),
            'pinterest_url': forms.TextInput(attrs={'class': 'form-control'}),
            
        }