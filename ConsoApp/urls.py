from django.urls import path
from ConsoApp import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('distribuidores', views.distribuidores, name="Distribuidores"),
    path('consolas', views.consolas, name="Consolas"),
    path('vendedores', views.vendedores, name="Vendedores"),
    path('busqueda',  views.busquedaConsola, name="busquedaConsola"),
    path('buscar/', views.buscar),

]