from django import forms
from BibliotecaWeb.models import Libros

class RegistroLibro(forms.ModelForm):

    
    class Meta:

         model = Libros
         fields = '__all__'