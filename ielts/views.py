from django.http import HttpResponse
from django.shortcuts import render

from classes.settings import TEMPLATES_DIR


# Create your views here.
def home(request):
    return render(request, 'home.html')
