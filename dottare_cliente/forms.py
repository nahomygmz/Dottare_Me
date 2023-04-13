from django import forms
from django.forms.widgets import DateTimeInput
from .models import Form_Contact
from .models import Form_Donacion

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Form_Contact
        fields = ['Nombre', 'Apellido', 'Email', 'Telefono', 'HorarioParaContactar', 'Mensaje']
        labels = {
            'Nombre': 'Nombre',
            'Apellido': 'Apellido',
            'Email': 'Email',
            'Telefono': 'Telefono',
            'HorarioParaContactar': '¿Cuándo prefieres que te contactemos?',
            'Mensaje': 'Mensaje',
        }
        widgets = {
            'HorarioParaContactar': DateTimeInput(attrs={'type': 'datetime-local'}),
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'Mensaje': forms.Textarea(attrs={'class': 'form-control'}),
        }

class DonacionForm(forms.ModelForm):
    class Meta:
        model = Form_Donacion
        fields = ['FullName', 'Email2', 'Telefono2', 'Monto']
        labels = {
            'FullName': 'Nombre completo',
            'Email2': 'Email',
            'Telefono2': 'Telefono',
            'Monto': 'Monto de la donación',
        }
        widgets = {
            'FullName': forms.TextInput(attrs={'class': 'form-control'}),
            'Email2': forms.EmailInput(attrs={'class': 'form-control'}),
            'Telefono2': forms.TextInput(attrs={'class': 'form-control'}),
            'Monto': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class AnimalSearchForm(forms.Form):
    OPTIONS = (
        ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('conejo', 'Conejo'),
        ('otros', 'Otros'),
    )
    
    busqueda = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'placeholder': 'Ingresa tu búsqueda aquí...'}))
    tipo = forms.ChoiceField(choices=OPTIONS, required=False, widget=forms.Select(attrs={'class': 'form-select'}))