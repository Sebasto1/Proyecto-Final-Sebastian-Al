from django.urls import path
from home import views
from django.contrib.auth.views import LogoutView




urlpatterns = [
   
    path('', views.home, name="home"),
    #path('distribuidores', views.distribuidores, name="Distribuidores"),
    #path('administrador', views.administrador, name="Administrador"),
    #path('empleados', views.empleados, name="Empleados"),
    #path('busqueda',  views.busquedaConsola, name="busquedaConsola"),
    #path('buscar/', views.buscar),
    path('caja',views.caja, name='caja'),

    

]