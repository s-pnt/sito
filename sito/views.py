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

from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone

def get_current_users():
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
    # Query all logged in users based on id list
    return User.objects.filter(id__in=user_id_list)

def prova(request):
    queryset = get_current_users()
    return render(request,
                  'sito/prova.html',
                  {'queryset': queryset.count()})