from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .forms import UserLoginForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            messages.success(request, f'{first_name} {last_name}, Kitab Klubumuza xoş gəldiniz, zəhmət olmasa sayta daxil olun.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form })


def loginUser(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            messages.success(request, f'{first_name} {last_name}, Kitab Klubumuza xoş gəldiniz, zövq almanız diləyi ilə!')
            return redirect('login')
    else:
        form = UserLoginForm
    return render(request, 'login.html', {'form': form })

def logoutUser(request):
    return render(request, 'logout.html')
