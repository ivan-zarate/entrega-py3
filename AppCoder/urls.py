from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('monitores/', views.getAllMonitors, name='Monitores'),
    path('notebooks/', views.getAllNotebooks, name='Notebooks'),
    path('amplificadores/', views.getAllAmplifiers, name='Amplificadores'),
    # path('signup/', views.signup, name='Signup'),
    path('monitor/agregar/', views.addProduct, name='addMonitor'),
    path('amplificador/agregar/', views.addProduct, name='addAmplifier'),
    path('notebook/agregar/', views.addProduct, name='addNotebook')
]
