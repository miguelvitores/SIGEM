from django.urls import path

from . import views

app_name = 'sigemapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('naves_nodrizas/listar/', views.ListarNaveNodrizasView.as_view(), name='listar_nn'),
    path('naves_nodrizas/crear/', views.CrearNaveNodrizasView.as_view(), name='crear_nn'),
]
