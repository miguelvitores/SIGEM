from django.db import models
from django.forms import ModelForm
from django.urls import reverse

class Marciano(models.Model):
    nombre = models.CharField(max_length=32)

    def __str__(self):
        return self.nombre


class NaveNodriza(models.Model):
    nombre = models.CharField(max_length=64)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('sigemapp:listar_nn')


class NaveNodrizaForm(ModelForm):
    class Meta:
        model = NaveNodriza
        fields = '__all__'


class Aeronave(models.Model):
    nombre = models.CharField(max_length=64)
    max_marcianos = models.IntegerField('aforo maximo nave', default=4)
    nave_origen = models.ForeignKey(NaveNodriza, related_name='nave_origen', on_delete=models.CASCADE)
    nave_destino = models.ForeignKey(NaveNodriza, related_name='nave_destino', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('sigemapp:listar_aeronaves')


class AsignarPasajero(models.Model):
    aeronave = models.ForeignKey(Aeronave, on_delete=models.CASCADE)
    pasajero = models.ForeignKey(Marciano, on_delete=models.CASCADE)

    def __str__(self):
        return self.aeronave.__str__() + " - " + self.pasajero.__str__()

    def get_absolute_url(self):
        return reverse('sigemapp:listar_ap')


class SeleccionarPasajeroBajar(models.Model):
    altaPasajero = models.ForeignKey(AsignarPasajero, on_delete=models.CASCADE , default=0)
    id = altaPasajero.__str__()

    def __str__(self):
        return self.altaPasajero.__str__()
    
    def get_absolute_url(self):
        return reverse('sigemapp:listar_ap')


class Revision(models.Model):
    id = models.IntegerField("id de la revision", primary_key=True)
    nombre_revisor = models.CharField('nombre del revisor', max_length=32)
    aeronave_revisada = models.ForeignKey(Aeronave, on_delete=models.CASCADE)
    fecha_revision = models.DateField('fecha de revision',auto_now=False, auto_now_add=False)
    pasajeros = models.ManyToManyField(Marciano)

    def __str__(self):
        return self.nombre_revisor + " - " + self.aeronave_revisada.__str__() + " - " + self.fecha_revision.__str__()

    def get_absolute_url(self):
        return reverse('sigemapp:listar_rev')
