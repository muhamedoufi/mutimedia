from django import forms
from django.contrib.auth.forms import UserCreationForm, User
from .models import Profile


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','is_staff','is_superuser', 'password1', 'password2']
        labels={
            'username' : 'Nom de l\'Utilisateur',
            'first_name' : 'Nom ',
            'last_name' : 'Prenom',
            # 'telephone' : 'Numéro Téléphone',
            'is_superuser': 'Medecin',
            'is_staff': 'Technicien'
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'image','manager']