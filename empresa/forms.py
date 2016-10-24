from django import forms

from .models import Datos

class MyForm(forms.ModelForm):

    class Meta:
        model = Datos
        fields = ('nombre_empresa', 'persona','pub_date' ,'puntuacion')
