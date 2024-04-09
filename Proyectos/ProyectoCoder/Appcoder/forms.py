from django import forms
from Appcoder.models import*
from django.contrib.auth.forms import UserCreationForm


class cursoformu(forms.Form):
  
    curso = forms.CharField()
    camada = forms.IntegerField()



class Profeformu(forms.Form):
  nombre = forms.CharField(max_length=60)
  apellido = forms.CharField(max_length=60)
  correo = forms.EmailField()
  profesion = forms.CharField(max_length=60) 

class UserRegistro(UserCreationForm):
   email = forms.EmailField()
   nombre = forms.CharField()
   apellido = forms.CharField()
   password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
   password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
    
   class Meta:
      model = User
      fields =  ["username", "email", "first_name", "last_name", "password1", "password2"]




class FormularioEditar(UserCreationForm):
   email = forms.EmailField()
   nombre = forms.CharField()
   apellido = forms.CharField()
   password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
   password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
    
   class Meta:
      model = User
      fields =  [ "email", "first_name", "last_name", "password1", "password2"]