from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.user_login, name='login'),
    path('landing_page', views.landing_page, name='landing_page'),
    path('logout/', views.logout_redirect, name='logout'),
    path('logout/', views.custom_logout, name='custom_logout'),  # Add this line

]
