from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from proapp.models import *
from proapp.forms import PositivoForm, VisitaForm, NegocioForm
from datetime import timedelta


# Create your views here.
def index(request):
	return render (request,'index.html', {'proapp':Positivo.objects.all()})


def alertar(request):
    if request.method == 'POST':
        form = PositivoForm(request.POST)
        if form.is_valid():
            positivo = form.save()
            inicio = positivo.fecha_test - timedelta(days=14)
            fin = positivo.fecha_test
            visitas = Visitas.objects.filter(fecha_visita__gte = inicio, fecha_visita__lte = fin, celular=positivo.celular)
            for visita in visitas:
                a = Alerta(negocio=visita.negocio,positivo=positivo)
                hora_inicio = visita.fecha_visita
                hora_fin = visita.fecha_visita+timedelta(int(visita.negocio.estancia))
                cercanos = Visitas.objects.filter(fecha_visita__gte=hora_inicio, fecha_visita__lte=hora_fin,negocio=visita.negocio).exclude(celular=positivo.celular)
                a.save()
                for persona in cercanos:
                    Cercano(aviso=a,tel_cercano=persona.celular).save()
            return redirect('index')
    else:
        form = PositivoForm()
        return render(request, 'alertar.html',{'form':form})


def registrarUsuario(request):
    if request.method == 'POST':
        form = UserCreationForm (request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate (username=username, password=password)
            login(request, user)
            return redirect('login')    
    else:
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form':form})


def home(request):
	return render(request, 'home.html')

def local(request):
	return render(request, 'local.html')
    

def filtrar(request):
	p = Positivo.objects.first()
	riesgo = Visitas.objects.filter(fecha_visita__gte=p.fecha_test)
	return render(request, 'filtrar.html',{'riesgo':riesgo})


def visitas(request):
	if request.method == 'POST':
		form = VisitaForm(request.POST)
		if form.is_valid():
			proapp = form.save()
			return redirect('index')
	else:
		form = VisitaForm()
		return render(request, 'visita.html',{'form':form}) 


def negocio(request):
	if request.method == 'POST':
		form = NegocioForm(request.POST)
		if form.is_valid():
			proapp = form.save()
			return redirect('home')
	else:
		form = NegocioForm()
		return render(request, 'regnegocio.html',{'form':form})
