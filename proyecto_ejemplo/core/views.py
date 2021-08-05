from django.shortcuts import render, redirect
from django.urls import reverse_lazy
import time

# Create your views here.
def index(request):

    if 'contador' in request.session:
        request.session['contador'] +=  1
    else:
        request.session['contador'] = 1

    return render(request, 'core/index.html')

def resetear(request):
    request.session['contador'] = 1
    return redirect(reverse_lazy('core:inicio'))



from time import gmtime, strftime, localtime
    
def tiempo(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "timelocal" : strftime("%Y-%m-%d %H:%M %p", localtime()),
    }
    return render(request,'core/index.html', context)


def procesar(request):

    request.POST['opcion']
    
    print("opcion: ", request.POST['opcion'])

    return redirect(reverse_lazy('core:inicio'))
    


def ejemplo(request):
    return render(request,"core/ejemplo-demo.html")


def crear_datos(request):
    print("voy a hacer algo.")

    if 'contador' not in request.session:
        request.session['contador'] = 1
    else:
        request.session['contador'] += 1

    # si no existe logs, lo crea, y punto.
    if 'logs' not in request.session:
        request.session['logs'] = []
    
    # a esta altura si o si existe logs.

    # if (request.session['contador'] % 2 == 0):
    #     color = "verde"
    # else:
    #     color = "rojo"

    datos_a_entregar = {
        'texto' : f"{request.session['contador']}  se creo a las:  {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}",
        'contador' : request.session['contador'],
        'esPar' : (request.session['contador'] % 2 == 0),
        'color' : 'verde' if (request.session['contador'] % 2 == 0) else 'rojo',
        'tiempo' : time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    }
    
    

    request.session['logs'].append(datos_a_entregar)
    request.session.save()



    return redirect("/ejemplo1/")

def vaciar_datos(request):
    if 'contador' in request.session:
        del request.session['contador']
    if 'logs' in request.session:
        del request.session['logs']

    print("DATOS LIMPIOS")
    return redirect("/ejemplo1/")
    
    