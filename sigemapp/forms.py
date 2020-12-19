import django.forms as forms

from .models import *
from datetime import date


class CreateAeronaveForm(forms.ModelForm):
    nombre = forms.CharField(max_length=64)
    max_marcianos = forms.IntegerField(help_text="aforo máximo nave", initial=4)
    nave_origen = forms.ModelChoiceField(
        label="Nave nodriza origen",
        queryset=NaveNodriza.objects.all()
    )
    nave_destino = forms.ModelChoiceField(
        label="Nave nodriza destino",
        queryset=NaveNodriza.objects.all()
    )

    class Meta:
        model = Aeronave
        fields = ['nombre', 'max_marcianos', 'nave_origen', 'nave_destino']
