from django.contrib import admin
from django.urls import path, re_path
from home import views
urlpatterns = [
    path("", views.index, name='home'),
    path("staff", views.staff, name='staff'),
    path("network", views.network, name='network'),
    path("servers", views.servers, name='servers'),
    path("software", views.software, name='software'),
    path("storage", views.storage, name='storage'),
    path("workstations", views.workstations, name='workstations'),
    path("aboutus", views.aboutus, name='aboutus'), 
 ]



