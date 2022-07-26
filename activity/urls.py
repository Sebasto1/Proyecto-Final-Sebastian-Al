from django.urls import path
from activity import views

urlpatterns = [
   

    #path('distribuidores', views.distribuidores, name="Distribuidores"),
    #path('administrador', views.administrador, name="Administrador"),
    #path('empleados', views.empleados, name="Empleados"),
    #path('busqueda',  views.busquedaConsola, name="busquedaConsola"),
    #path('buscar/', views.buscar),
    #path('administrador', views.administradores, name="Administrador"),
    #path('administrador/lista', views.AdministradorLista.as_view(), name='Lista'),
    # path(r'^(?P<pk>\d+)$', views.AdministradorDetalle.as_view(), name='Detalle'),
    # path(r'^nuevo$', views.AdministradorCreacion.as_view(), name='New'),
    # path(r'^editar/(?P<pk>\d+)$', views.AdministradorUpdate.as_view(), name='Edit'),
    # path(r'^borrar/(?P<pk>\d+)$', views.AdministradorDelete.as_view(), name='Delete'),
    path('employee/list', views.DistribuidoresList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.DistribuidoresDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.DistribuidoresCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.DistribuidoresUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.DistribuidoresDelete.as_view(), name='Delete'),
    path('caja',views.caja, name='caja'),

    

]