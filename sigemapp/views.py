from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import *


class IndexView(generic.TemplateView):
    template_name = 'sigemapp/index.html'


class CrearNaveNodrizasView(generic.CreateView):
    template_name = 'sigemapp/crear_nn.html'

    def get_queryset(self):
        return NaveNodriza.objects.all()


class ListarNaveNodrizasView(generic.ListView):
    template_name = 'sigemapp/listar_nn.html'
    context_object_name = 'naves_nodrizas'

    def get_queryset(self):
        return NaveNodriza.objects.all()
