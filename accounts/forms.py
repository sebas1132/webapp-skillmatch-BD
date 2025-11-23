from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
import re

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'input-field',
            'placeholder': 'usuario@inacap.cl',
            'required': 'required'
        })
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input-field',
            'placeholder': 'Contraseña',
            'required': 'required'
        })
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input-field',
            'placeholder': 'Confirmar Contraseña',
            'required': 'required'
        })
    )
    
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Validar que sea un correo de INACAP
        if not re.match(r'^[a-zA-Z0-9._%+-]+@(inacap\.cl|inacapmail\.cl)$', email):
            raise ValidationError(
                'Solo se permiten correos corporativos de INACAP (@inacap.cl o @inacapmail.cl)'
            )
        
        if User.objects.filter(email=email).exists():
            raise ValidationError('Este correo ya está registrado')
        
        return email

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'input-field',
            'placeholder': 'usuario@inacap.cl',
            'required': 'required'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input-field',
            'placeholder': 'Contraseña',
            'required': 'required'
        })
    )

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'input-field',
            'placeholder': 'usuario@inacap.cl',
            'required': 'required'
        })
    )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r'^[a-zA-Z0-9._%+-]+@(inacap\.cl|inacapmail\.cl)$', email):
            raise ValidationError(
                'Solo se permiten correos corporativos de INACAP (@inacap.cl o @inacapmail.cl)'
            )
        return email