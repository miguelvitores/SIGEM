from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import *
from .forms import *


class IndexView(generic.TemplateView):
    template_name = 'sigemapp/index.html'


class ListarNaveNodrizasView(generic.ListView):
    template_name = 'sigemapp/listar_nn.html'
    context_object_name = 'naves_nodrizas'

    def get_queryset(self):
        return NaveNodriza.objects.all()


class NaveNodrizaCreate(generic.edit.CreateView):
    model = NaveNodriza
    fields = '__all__'


class ListarAeronavesView(generic.ListView):
    template_name = 'sigemapp/listar_aeronaves.html'
    context_object_name = 'aeronaves'

    def get_queryset(self):
        return Aeronave.objects.all()


class AeronaveCreate(generic.edit.CreateView):
    model = Aeronave
    form_class = CreateAeronaveForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AsignarPasajeroCreate(generic.edit.CreateView):
    model = AsignarPasajero
    form_class = CreateAsignarPasajeroForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ListarAsignarPasajeroView(generic.ListView):
    template_name = 'sigemapp/listar_ap.html'
    context_object_name = 'asignar_pasajero'

    def get_queryset(self):
        return AsignarPasajero.objects.all()


class BajarPasajeroCreate(generic.edit.CreateView):
    model = BajarPasajero
    form_class = CreateBajarPasajeroForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ListarBajarPasajeroView(generic.ListView):
    template_name = 'sigemapp/listar_bp.html'
    context_object_name = 'bajar_pasajero'

    def get_queryset(self):
        return BajarPasajero.objects.all()
