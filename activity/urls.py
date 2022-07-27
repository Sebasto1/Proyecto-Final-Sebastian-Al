from django.urls import path
from activity import views

urlpatterns = [
   

    path('distribuidores_registro', views.distribuidores_registro, name="distribuidores_registro"),
    path('distribuidores/list', views.DistribuidoresList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.DistribuidoresDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.DistribuidoresCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.DistribuidoresUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.DistribuidoresDelete.as_view(), name='Delete'),
    path('work_employee',views.work_employee, name='work_employee'),
    path('work_admin',views.work_admin, name='work_admin'),
    path('distribuidores',views.distribuidores, name='distribuidores'),

    

]