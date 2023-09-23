from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import User

# Create your views here.
def signin(request):
  return render(request, 'login.html');

def signup(request):
  return render(request, 'register.html')

def store(request):
  name = request.POST['name']
  lastname = request.POST['lastname']
  password = request.POST['password']

  user = User(
    name= name,
    lastname= lastname,
    password= password
  )
  user.save()
  return render(request, 'login.html')

def auth(request):
  lastname = request.POST['lastname']
  password = request.POST['password']
  # Intentar autenticar al usuario
  
  try:
    # Buscar al usuario por nombre_de_usuario
    user = User.objects.get(lastname= lastname)

    # Verificar la contraseña
    if user.password == password:
      # Contraseña válida, inicia sesión
      return redirect('formapp')
    else:
      # Contraseña incorrecta, muestra un mensaje de error
      HttpResponse('Contraseña incorrecta.')

  except User.DoesNotExist:
    # El usuario no existe, muestra un mensaje de error
    HttpResponse('El usuario no existe. Por favor, regístrate o verifica tus credenciales.')