from django.shortcuts import render, redirect
from .forms import UserRegForm
from django.contrib import messages
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        form = UserRegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Вітаємо, користувача було створено')
            return redirect('home')
    else:
        form = UserRegForm()
    return render(request, 'users/registration.html', {'form': form})

def profile(request):
    return render(request, 'users/profile.html')
