# dashboard/forms.py

from django import forms
from accounts.models import Usuario
from django.contrib.auth.hashers import make_password

class RegistroUsuarioForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput
    )

    class Meta:
        model = Usuario
        fields = [
            'id_usuario',
            'nombre',
            'apellido',
            'correo_institucional',
            'carrera',
        ]

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')

        if p1 != p2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.password_hash = make_password(self.cleaned_data['password1'])
        usuario.rol = "Estudiante"
        usuario.estado_cuenta = "Activo"

        if commit:
            usuario.save()

        return usuario
