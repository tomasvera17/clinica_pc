from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'tipo_usuario', 'telefono', 'direccion']
    
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'password1' or field_name == 'password2':
                field.help_text = ''  
