from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            return redirect('success')

    return render(request, 'myapp/register.html', {'form': form})


def success(request):
    return render(request, 'myapp/success.html')