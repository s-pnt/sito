from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('python/introduzione/', views.python_introduzione, name='python_introduzione'),
    path('python/installazione/', views.python_installazione, name='python_installazione'),
    path('python/shell/', views.python_shell, name='python_shell'),
    path('python/script/', views.python_script, name='python_script'),
    path('python/variabili/', views.python_variabili, name='python_variabili'),
    path('python/stringhe/', views.python_stringhe, name='python_stringhe'),
    path('python/liste/', views.python_liste, name='python_liste'),
    path('python/tuple/', views.python_tuple, name='python_tuple'),
    path('python/operatori/', views.python_operatori, name='python_operatori'),
    path('python/dizionari/', views.python_dizionari, name='python_dizionari'),
    path('python/insiemi/', views.python_insiemi, name='python_insiemi'),
    path('python/riassunto_dati/', views.python_riassunto_dati, name='python_riassunto_dati'),
    path('linux/introduzione/', views.linux_introduzione, name='linux_introduzione'),
    path('linux/distribuzioni/', views.linux_distribuzioni, name='linux_distribuzioni'),
    path('raspberrypi/introduzione/', views.raspberrypi_introduzione, name='raspberrypi_introduzione'),
]