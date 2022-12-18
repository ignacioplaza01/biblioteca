from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from BibliotecaWeb.models import Libros
from BibliotecaWeb.forms import RegistroLibro

@login_required

def index(request):
    libro = Libros.objects.all()
    data = {'Libro':libro}
    return render(request, 'Index/index.html',data)

