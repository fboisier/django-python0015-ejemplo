from django.shortcuts import render, redirect

# Create your views here.
def formulario(request):
    if request.method == 'POST':
        print(request.POST)
        resultado = 0

        if request.POST['opcion'] == "1":
            resultado = int(request.POST['operando1']) + int(request.POST['operando2'])

        if request.POST['opcion'] == "2":
            resultado = int(request.POST['operando1']) - int(request.POST['operando2'])

        if request.POST['opcion'] == "3":
            resultado = int(request.POST['operando1']) * int(request.POST['operando2'])

        if request.POST['opcion'] == "4":
            resultado = int(request.POST['operando1']) / int(request.POST['operando2'])

        request.session['resultado'] = resultado

        return redirect('/formulario/resultado/')

    if request.method == 'GET':
        return render(request, 'formulario/formulario.html')

def resultado(request):
    return render(request, 'formulario/resultado.html')