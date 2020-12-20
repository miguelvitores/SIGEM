from django.urls import path

from . import views

app_name = 'sigemapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('naves_nodrizas/listar/', views.ListarNaveNodrizasView.as_view(), name='listar_nn'),
    path('naves_nodrizas/crear/', views.NaveNodrizaCreate.as_view(), name='crear_nn'),
    path('aeronaves/listar/', views.ListarAeronavesView.as_view(), name='listar_aeronaves'),
    path('aeronaves/crear/', views.AeronaveCreate.as_view(), name='crear_aeronave'),
    path('gestionar_pasajero/listar/', views.ListarAsignarPasajeroView.as_view(), name='listar_ap'),
    path('gestionar_pasajero/crear/', views.AsignarPasajeroCreate.as_view(), name='crear_ap'),
    path('gestionar_pasajero/<pk>/bajar/', views.BajarPasajero.as_view()),
    path('gestionar_pasajero/bajar/', views.SeleccionarPasajeroBajar.as_view(), name='bajar_ap'),
    path('revisar/listar/', views.ListarRevisionView.as_view(), name='listar_rev'),
    path('revisar/crear/', views.RevisionCreate.as_view(), name='crear_rev')
]
