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


class BajarPasajero(models.Model):
    aeronave = models.ForeignKey(Aeronave, on_delete=models.CASCADE)
    pasajero = models.ForeignKey(Marciano, on_delete=models.CASCADE)

    def __str__(self):
        return self.aeronave.__str__() + " - " + self.pasajero.__str__()

    def get_absolute_url(self):
        return reverse('sigemapp:listar_bp')


class Revision(models.Model):
    nombre_revisor = models.CharField('nombre del revisor', max_length=32)
    aeronave_revisada = models.ForeignKey(Aeronave, on_delete=models.CASCADE)
    fecha_revision = models.DateTimeField('fecha de revision')
    pasajeros = models.ManyToManyField(Marciano)

    def __str__(self):
        return self.nombre_revisor + " - " + self.aeronave_revisada.__str__()
