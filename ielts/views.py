from django.http import HttpResponse
from django.shortcuts import render

from classes.settings import TEMPLATES_DIR


# Create your views here.
def home(request):
    return render(request, 'home.html')


def courses(request):
    return render(request, 'courses.html')


def about_us(request):
    return render(request, 'about_us.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')


def register(request):
    return render(request, 'register.html')


def products(request):
    return render(request, 'products.html')


def cart(request):
    return render(request, 'cart.html')


def orders(request):
    return render(request, 'order.html')


def payments(request):
    return render(request, 'payment.html')


def subscriptions(request):
    return render(request, 'subscription.html')



