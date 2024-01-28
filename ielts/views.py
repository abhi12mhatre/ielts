from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def home(request):
    return render(request, 'home.html')


def courses(request):
    return render(request, 'courses.html')


def about_us(request):
    return render(request, 'about_us.html')


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('home')  # Change 'home' to the desired URL after successful login
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'messages': messages})


def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')  # Change 'home' to the desired URL after successful logout


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')  # Change 'home' to the desired URL after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form, 'messages': messages})


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
