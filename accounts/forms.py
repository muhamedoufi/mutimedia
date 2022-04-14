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
        widgets={
            'password1':forms.PasswordInput(attrs={'placeholder':'********','autocomplete':'off','data-toggle':'password'}),
        }
        help_texts={
            "is_superuser":"Designates whether the user when is Medecin",
            'is_staff': 'Designates whether the user when is Technicien',
        }
    def __init__(self, *args, **kwargs):
     
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['is_staff'].required=True
        self.fields['is_superuser'].required=False

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'image','manager']