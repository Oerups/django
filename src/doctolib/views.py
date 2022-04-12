from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserCreationForm, PracticianUpdateForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            group = Group.objects.get(name='patient')
            group.user_set.add(user.id)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def practician_profile(request):
    if request.method == 'POST':
        form = PracticianUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('practician_profile')
    else:
        form = PracticianUpdateForm(instance=request.user)

    return render(request, 'practician/profile.html', {'form': form})