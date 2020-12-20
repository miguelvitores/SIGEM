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


class CreateAsignarPasajeroForm(forms.ModelForm):
    aeronave = forms.ModelChoiceField(
        label="Aeronave",
        queryset=Aeronave.objects.all()
    )
    pasajero = forms.ModelChoiceField(
        label="Marciano que se sube a la aeronave",
        queryset=Marciano.objects.all()
    )

    class Meta:
        model = AsignarPasajero
        fields = ['aeronave', 'pasajero']


class BajarPasajeroForm(forms.ModelForm):
    altaPasajero = forms.ModelChoiceField(
        label="Pasajero",
        queryset=AsignarPasajero.objects.all()
    )
    class Meta:
        model = SeleccionarPasajeroBajar
        fields = ['altaPasajero']

class RevisarAeronaveForm(forms.ModelForm):

    aeronave_revisada = forms.ModelChoiceField(
        label="Aeronave Revisada",
        queryset=Aeronave.objects.all()
    )
    class Meta:
        model = Revision
        fields = ['id','nombre_revisor', 'aeronave_revisada', 'fecha_revision']
        widgets = {
        'fecha_revision': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }