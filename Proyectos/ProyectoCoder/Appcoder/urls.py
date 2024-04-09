from django.urls import path
from Appcoder.views import * 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name="Inicio"),
    path('cursos/', Curso, name="Cursito"),
    path('profesores/', profesor, name="Profesores"),
    path('entregables/', entregable, name="Entregables"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path("cursoformu/", CursoFormulario, name="formulariocurso"),
    path("leerprofesores/", leerprofesores, name="ProfesLeer" ),
    path("Crearprofes/", Crearprofesores, name="ProfesCrear" ),
    path("eliminarprofes/<profeNombre>", eliminarprofesores, name="eliminarprofesores" ),
    path("login/", InicioSesion, name="Login"),
    path("register/", register, name="Registro"),
    path("logout/", LogoutView.as_view(template_name="Appcoder/logout.html"), name= "Logout"),
    path("editar/", editarPerfil, name= "EditarPerfil"),

]



