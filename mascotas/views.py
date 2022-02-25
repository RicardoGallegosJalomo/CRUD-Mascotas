from django.shortcuts import render, redirect
from .models import Mascota
from .forms import MascotaForm
from django.views.generic import TemplateView,ListView

def home(request):

	datos = Mascota.objects.all()
	context = {'datos':datos}
	return render(request,'mascotas/home.html', context)

def agregar(request):
	
	if request.method == "POST":
		form = MascotaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = MascotaForm()

	context = {'form':form}
	return render(request,'mascotas/agregar.html',context)

def eliminar(request,id):
	iddelete = Mascota.objects.get(id=id)
	iddelete.delete()
	return redirect("home")

def editar(request, id):
	idedit = Mascota.objects.get(id=id)
	if request.method == 'POST':
		form = MascotaForm(request.POST, instance=idedit)
		if form.is_valid():
			form.save()
			return redirect("home")
	else:
		form = MascotaForm(instance=idedit)

	context = {"form": form}
	return render(request, "mascotas/editar.html", context)


