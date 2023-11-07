from django import forms 
from .models import Monitores, Amplificadores, Notebooks, Usuarios

class MonitoresForm(forms.ModelForm):
    class Meta:
        model = Monitores
        fields=['nombre', 'precio','cantidad', 'tamaño', 'imagen']
        

class AmplificadoresForm(forms.ModelForm):
    class Meta:
        model = Amplificadores
        fields=['nombre', 'precio','cantidad', 'potencia', 'imagen']
        

class NotebooksForm(forms.ModelForm):
    class Meta:
        model = Notebooks
        fields=['nombre', 'precio','cantidad','imagen']
        
        
class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields=['nombre', 'apellido','edad', 'email', 'password']