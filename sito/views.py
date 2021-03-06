from django.shortcuts import render

def home(request):
    return render(request,
                  'sito/home.html',
                  {})

def python_introduzione(request):
    return render(request,
                  'sito/python_introduzione.html',
                  {})

def python_installazione(request):
    return render(request,
                  'sito/python_installazione.html',
                  {})

def python_shell(request):
    return render(request,
                  'sito/python_shell.html',
                  {})

def python_script(request):
    return render(request,
                  'sito/python_script.html',
                  {})

def python_variabili(request):
    return render(request,
                  'sito/python_variabili.html',
                  {})

def python_stringhe(request):
    return render(request,
                  'sito/python_stringhe.html',
                  {})

def python_liste(request):
    return render(request,
                  'sito/python_liste.html',
                  {})

def python_tuple(request):
    return render(request,
                  'sito/python_tuple.html',
                  {})

def python_operatori(request):
    return render(request,
                  'sito/python_operatori.html',
                  {})

def python_dizionari(request):
    return render(request,
                  'sito/python_dizionari.html',
                  {})

def python_insiemi(request):
    return render(request,
                  'sito/python_insiemi.html',
                  {})

def python_riassunto_dati(request):
    return render(request,
                  'sito/python_riassunto_dati.html',
                  {})

def linux_introduzione(request):
    return render(request,
                  'sito/linux_introduzione.html',
                  {})

def linux_distribuzioni(request):
    return render(request,
                  'sito/python_introduzione.html',
                  {})

def raspberrypi_introduzione(request):
    return render(request,
                  'sito/raspberrypi_introduzione.html',
                  {})