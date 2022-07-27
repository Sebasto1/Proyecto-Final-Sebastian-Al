from django.urls import path
from home import views
from django.contrib.auth.views import LogoutView




urlpatterns = [
   
    path('', views.home, name="home"),

    

]