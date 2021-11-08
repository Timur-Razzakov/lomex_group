from django.shortcuts import render
from .models import Actor, Writer, Movie


def index(request):
    return render(request, 'mainapp/index.html', )
