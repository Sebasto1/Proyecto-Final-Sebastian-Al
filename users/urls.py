from django.urls import path, include
from users import views
from django.contrib.auth.views import LogoutView
from .views import RegisterViewAdmin, RegisterViewEmployee
from users.models import *

urlpatterns = [
    
    path('profile/', views.profile, name='users-profile'),
    path('login', views.login_request, name='login'),
    path('register_employee/', RegisterViewEmployee.as_view(), name='register_employee'),
    path('logout', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/',views.register, name='register'),
    path('register_admin/', RegisterViewAdmin.as_view(), name='register_admin'),
 


]