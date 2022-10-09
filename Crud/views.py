from enum import unique
from django.shortcuts import render, HttpResponse, redirect
from requests import request
from .forms import ContactoForm
# Create your views here.
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import misRutas, sitioTuristico, Region
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def Login(request):
    return render(request, "Crud/Login.html")


def Register(request):
    return render(request, "Crud/Register.html")


def sitioRegion(request, region):
    posts = Region.objects.get(region=region)
    sitios = sitioTuristico.objects.filter(region=region)
    return render(request, "Crud/region.html", {"posts": posts, "sitios": sitios})


def SitioTuristico(request, region, nombre):
    if request.method == 'GET':
        posts = sitioTuristico.objects.get(region=region, nombre=nombre)
        return render(request, "Crud/sitioTuristico.html", {"posts": posts})
    elif request.method == 'POST':
        posts = sitioTuristico.objects.get(region=region, nombre=nombre)
        rutas = misRutas(username=request.user.username,
                         nombre=sitioTuristico.objects.get(
                             nombre=nombre).nombre,
                         ubicacion=sitioTuristico.objects.get(
                             nombre=nombre).ubicacion,
                         precio=sitioTuristico.objects.get(
                             nombre=nombre).precio)
        rutas.save()
        return render(request, "Crud/sitioTuristico.html", {"posts": posts})


def Inicio(request):
    sitios = sitioTuristico.objects.filter(sitioFavorito=True)
    return render(request, "Crud/inicio.html", {"sitios": sitios})


def Contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data['form'] = formulario
    return render(request, "Crud/contacto.html", data)


@login_required(login_url='/iniciar-sesion')
def MiPerfil(request, username):
    rutas = misRutas.objects.filter(username=username)
    return render(request, "Crud/mi-perfil.html", {'rutas': rutas})


class VRegistro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "Crud/Register.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('Inicio')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "Crud/Register.html", {"form": form})


def cerrar_sesion(request):
    logout(request)
    return redirect('Inicio')


def logear(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('Inicio')
            else:
                messages.error(request, "Usuario no valido")
        else:
            messages.error(request, "Informacion no valida")

    form = AuthenticationForm()
    return render(request, "Crud/Login.html", {"form": form})
