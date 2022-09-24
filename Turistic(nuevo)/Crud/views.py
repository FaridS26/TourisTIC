from django.shortcuts import render, HttpResponse, redirect
from .forms import ContactoForm
# Create your views here.
from django.views.generic import View
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def Login(request):

    return render(request, "Crud/Login.html")


def Register(request):

    return render(request, "Crud/Register.html")


def Region_Andina(request):

    return render(request, "Crud/region-andina.html")


def Sitio1(request):

    return render(request, "Crud/sitio1.html")


def Inicio(request):

    return render(request, "Crud/inicio.html")


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


def MiPerfil(request):
    return render(request, "Crud/mi-perfil.html")


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
