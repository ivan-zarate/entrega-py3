from django.shortcuts import render, redirect
from .models import Notebooks, Amplificadores, Monitores, Usuarios
from .forms import AmplificadoresForm, NotebooksForm, MonitoresForm, UsuariosForm


def inicio(req):
    result=req.GET.get("Buscar")
    if result:
        notebooks=Notebooks.objects.filter(nombre=result)
        return render(req, "index.html", {"notebooks":notebooks}) 
    else:
        return render(req, "index.html")

def getAllMonitors(req):
    productos = Monitores.objects.all()
    return render(req, "monitores.html", {"productos":productos})

def getAllNotebooks(req):
    productos = Notebooks.objects.all()
    return render(req, "notebooks.html", {"productos":productos})

def getAllAmplifiers(req):
    productos = Amplificadores.objects.all()
    return render(req, "amplificadores.html", {"productos":productos})

def addProduct(req):
    response=req.headers
    if req.method == "POST":
        if response['Referer']=='http://127.0.0.1:8000/AppCoder/amplificador/agregar/':
            newProduct= AmplificadoresForm(req.POST)
            if newProduct.is_valid():
                product=newProduct.save()
                return redirect("Inicio")
        elif response['Referer']=='http://127.0.0.1:8000/AppCoder/monitor/agregar/':
            newProduct= MonitoresForm(req.POST)
            if newProduct.is_valid():
                product=newProduct.save()
                return redirect("Inicio")
        elif response['Referer']=='http://127.0.0.1:8000/AppCoder/notebook/agregar/':
            newProduct= NotebooksForm(req.POST)
            if newProduct.is_valid():
                product=newProduct.save()
                return redirect("Inicio")
    elif response['Referer']=='http://127.0.0.1:8000/AppCoder/amplificadores/':
        newProduct= AmplificadoresForm()
        return render(req,"addProduct.html", {'newProduct':newProduct} )
    elif response['Referer']=='http://127.0.0.1:8000/AppCoder/monitores/':
        newProduct= MonitoresForm()
        return render(req,"addProduct.html", {'newProduct':newProduct} )
    elif response['Referer']=='http://127.0.0.1:8000/AppCoder/notebooks/':
        newProduct= NotebooksForm()
        return render(req,"addProduct.html", {'newProduct':newProduct} )
    