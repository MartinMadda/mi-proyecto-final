from cProfile import label
from django import forms
from ejemplo.models import Familiar, Empresa, Mascota

class Buscar(forms.Form):
  nombre = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = [
      'nombre',
      'apellido',
      'direccion', 
      'email',
      'fecha_de_nacimiento', 
      'numero_pasaporte' 
    ]
    widgets = {
      'nombre':forms.TextInput(attrs={'placeholder':'Nombre'}),
      'apellido':forms.TextInput(attrs={'placeholder':'Apellido'}),
      'direccion':forms.TextInput(attrs={'placeholder':'direccion'}),
      'email':forms.EmailInput(attrs={'placeholder':'ejemplo@gmail.com'}),
      'fecha_de_nacimiento': forms.DateInput(attrs={'type':'date'}),
      'numero_pasaporte':forms.NumberInput(attrs={'placeholder':'Pasaporte N°'})
      }
class EmpresaForm(forms.ModelForm):
  class Meta:
    model = Empresa
    fields = [
      'nombre_empresa',
      'url_empresa',
      'telefono', 
    ]
    widgets = {
      'nombre_empresa':forms.TextInput(attrs={'placeholder':'Nombre de Empresa'}),
      'url_empresa':forms.TextInput(attrs={'placeholder':'url_empresa'}),
      'telefono':forms.NumberInput(attrs={'placeholder':'telefono'}),

      }

class MascotaForm(forms.ModelForm):
  class Meta:
    model = Mascota
    fields = [
      'nombre_mascota',
      'animal',
      'telefono_dueño', 
    ]
    widgets = {
      'nombre_mascota':forms.TextInput(attrs={'placeholder':'Nombre de la Mascota'}),
      'animal':forms.TextInput(attrs={'placeholder':'Que animal es'}),
      'telefono_dueño':forms.NumberInput(attrs={'placeholder':'telefono del dueño'}),
      }