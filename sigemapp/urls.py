from django.urls import path

from . import views

app_name = 'sigemapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('naves_nodrizas/listar/', views.ListarNaveNodrizasView.as_view(), name='listar_nn'),
    path('naves_nodrizas/crear/', views.NaveNodrizaCreate.as_view(), name='crear_nn'),
    path('aeronaves/listar/', views.ListarAeronavesView.as_view(), name='listar_aeronaves'),
    path('aeronaves/crear/', views.AeronaveCreate.as_view(), name='crear_aeronave'),
]
