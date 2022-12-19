from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from BibliotecaWeb.models import Libros
from django.db.models import Q
from BibliotecaWeb.forms import RegistroLibro

@login_required

def index(request):
  
  libros = Libros.objects.all()
  busqueda = request.GET.get("buscar")
  if busqueda:
    libros = Libros.objects.filter(
      Q(Titulo__icontains = busqueda) |
      Q(Autor__icontains = busqueda) |
      Q(Genero__icontains = busqueda)
    ).distinct()

  return render(request, 'index/index.html',{'Libro':libros})

def usuario(request):
    return render(request, 'prestamos/prestamos.html')

def cerrarSesion(request):
  logout(request)
  return redirect('/')    