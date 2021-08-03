from django.shortcuts import render, redirect

# Create your views here.
def index(request):

    if 'contador' in request.session:
        request.session['contador'] +=  1
    else:
        request.session['contador'] = 1

    return render(request, 'core/index.html')

def resetear(request):
    request.session['contador'] = 1
    return redirect("/")