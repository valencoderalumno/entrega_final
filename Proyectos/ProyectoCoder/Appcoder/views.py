from django.shortcuts import render
from django.http import HttpResponse
from Appcoder.models import Curso, Profesor
from Appcoder.forms import *
from django.contrib.auth.forms import AuthenticationForm,  UserCreationForm
from django.contrib.auth import login, authenticate


# Create your views here.


def InicioSesion(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "Appcoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "Appcoder/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "Appcoder/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "Appcoder/login.html", {"form": form})



# Vista de registro
def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserCreationForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserCreationForm()     

      return render(request,"AppCoder/registro.html" ,  {"form":form})


def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = FormularioEditar(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "Appcoder/inicio.html")

    else:

        miFormulario = FormularioEditar(initial={'email': usuario.email})

    return render(request, "Appcoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
































def inicio(request):
  return render(request,"Appcoder/inicio.html")

def Curso(request):

 cur1 = Curso(nombre="Python", camada=43125)
 cur1.save

 return HttpResponse(f"El curso que he creado es: {cur1.nombre} y su camada es: {cur1.camada}")

def estudiantes(request):
  return  render(request,"Appcoder/estudiantes.html")

def profesor(request):
  return render(request,"Appcoder/profesores.html")

def entregable(request):
  return render(request,"Appcoder/entregables.html")

def CursoFormulario(request):

 if request.method == "POST":
   
   
   formulario1 = cursoformu(request.POST)
   

   if formulario1.is_valid():
       
          info = formulario1.cleaned_data

          curso = Curso(nombre=info["curso"], camada=info["camada"])
 
          curso.save()
  
          return render(request, "/Appcoder/inicio.html") 

 else:

     formulario1 = cursoformu()
 
 return render(request, "Appcoder/cursoformulario.html", {"form1": formulario1})





def leerprofesores(request):
 
   profesor = profesor.object.all()

   contexto = {"teachers": profesor}

   return render(request, "Appcoder/leerprofes.html", contexto) 






def Crearprofesores(request):
  if request.method == "POST":
   
   formulario2 = Profeformu(request.POST)

   if formulario2.is_valid():
       
       info = formulario2.cleaned_data

       profesor.nombre = info["nombre"]
       profesor.apellido = info["apellido"]
       profesor.correo = info["correo"]
       profesor.profesion = info["profesion"]

 
       profesor.save()
  
       return render(request, "/Appcoder/inicio.html") 

   else:

     formulario2 = Profeformu()
 
  return render(request, "Appcoder/profeformulario.html", {"form2": formulario2})


def eliminarprofesores (request, profeNombre):
   profesor = Profesor.objects.get(nombre=profeNombre)
   profesor.delete()

   profesores = Profesor.objects.all()
   contexto = {"teachers": profesores}

   return render(request, "Appcoder/leerprofes.html", contexto)




