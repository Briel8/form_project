from django import forms
from .models import User
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'

        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if ' ' in username:
            raise ValidationError('username must not contain spaces.')
        
        return username
    
class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if ' ' in username:
            raise ValidationError('username must not contain spaces.')
        
        return username