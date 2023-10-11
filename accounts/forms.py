from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']



        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'password1': forms.PasswordInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']


        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            
            
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city','phone_num','image']

        
        widgets = {
           
        
            'phone_num': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            
            
            
        }