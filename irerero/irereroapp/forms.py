from django import forms
from .models import Class
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    email = forms.EmailField(required=True, label="Email")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Password")
class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['profile_picture', 'name', 'teacher']
        widgets = {
            'teacher': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Class Name'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }

