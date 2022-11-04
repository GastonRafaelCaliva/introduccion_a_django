from django.shortcuts import render

# Create your views here.
from portfolio.models import Proyecto

def projectIndex(request):
    proyectos = Proyecto.objects.all()
    context = {
        'proyectos': proyectos
    }
    return render(request, 'projectIndex.html', context)

def projectDetail(request,pk):
    proyecto = Proyecto.objects.get(pk=pk)
    context = {
        'proyecto': proyecto
    }
    return render(request, 'projectDetail.html', context)