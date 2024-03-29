from django.urls import path

from AppCoder import views

urlpatterns = [


    path('', views.inicio, name="inicio"),
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    path('busquedaCamada', views.busquedaCamada, name="busquedaCamada"),
    path('buscar', views.buscar, name="buscar"),
    path('leerProfesores', views.leerProfesores, name="leerProfesores"),

]