from django.shortcuts import render, HttpResponse
# Create your views here.

def Login(request):

	return render(request, "Crud/Login.html")

def Register(request):

	return render(request, "Crud/Register.html")

def Region_Andina(request):

	return render(request, "Crud/region-andina.html")

def Contacto(request):

	return render(request, "Crud/contacto.html")

def Sitio1(request):

	return render(request, "Crud/sitio1.html")

def Index(request):

	return render(request, "Crud/index.html")