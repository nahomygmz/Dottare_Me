from django.contrib import admin
from django.urls import path, include
from dottare_cliente import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adoptar/', views.adoptar, name='adoptar'),
    path('buscar_resultados/', views.buscar_resultados, name='buscar_resultados'),
    path('error/', views.error, name='error'),
    path('perfil_animal/', views.perfil_animal, name='perfil_animal'),
    path('descargar_pdf/<str:file_name>/', views.download_file, name='descargar_pdf'),
    path('como_adoptar/', views.como_adoptar, name='como_adoptar'),
    path('about/', views.about, name='about'),
    path('donacion/', views.donacion, name='donacion'),
    path('contacto/', views.contacto, name='contacto'), 
    path('admin/', admin.site.urls),  
    path('', include('admin_material.urls')),
  
]