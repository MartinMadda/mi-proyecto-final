from cProfile import label
from django import forms
from ejemplo.models import Familiar

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
      'direccion':forms.TextInput(attrs={'placeholder':'Ejemplo 123'}),
      'email':forms.EmailInput(attrs={'placeholder':'ejemplo@gmail.com'}),
      'fecha_de_nacimiento': forms.DateInput(attrs={'type':'date'}),
      'numero_pasaporte':forms.NumberInput(attrs={'placeholder':'Pasaporte N°'})
      }
    