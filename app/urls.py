from os import name
from django.urls import path
from . import views


app_name = 'app'

urlpatterns = [
    path('', views.inicio,name='inicio'),
    path('login/',views.login_user,name='login'),
    path('private/', views.private,name='private'),
    path('examenes/', views.listar_examenes,name='examenes'),
    path('crearexamen/', views.crear_examen,name='crearexamen'),
    path('<pk>/editar_examen/', views.editar_examen, name='editar_examen'),
    path('<pk>/eliminar/', views.eliminar_examen, name='eliminar_examen'),
    path('graficos/', views.graficos,name='graficos'),  
    path('agendar/', views.agendar,name='agendar'),
    path('agregar_usuario_db/', views.agregar_usuario_db,name='agregar_usuario_db'),
    path('<rut>/eliminar_pacientes_db', views.eliminar_pacientes_db, name='eliminar_pacientes_db'),
    path('<rut>/editar_paciente_db', views.editar_paciente_db, name='editar_paciente_db'),
]
