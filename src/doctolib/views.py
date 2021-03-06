from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserCreationForm, PracticianUpdateForm, TicketCreationForm, SlotCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .models import *
from django.contrib.auth.decorators import login_required

def index(request):
    geoLocations = GeoLocation.objects.all()

    if request.method == 'POST':
        geoLocation = request.POST.get('geoLocation')
        practicians = User.objects.all().filter(geo_location=geoLocation)

        return render(request, 'index.html', {'geoLocations': geoLocations, 'practicians': practicians, 'selectedLocation': geoLocation})

    return render(request, 'index.html', {'geoLocations': geoLocations})

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

def register_practician(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            group = Group.objects.get(name='practician')
            group.user_set.add(user.id)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register_practician.html', {'form': form})

@login_required
def practician_profile(request):
    if request.method == 'POST':
        form = PracticianUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

    return redirect('practician')

@login_required
def practician_tickets(request):
    if request.method == 'POST':
        form = TicketCreationForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()

    return redirect('practician')

@login_required
def practician(request):
    formUser = PracticianUpdateForm(instance=request.user)
    formTickets = TicketCreationForm()
    tickets = Ticket.objects.filter(user=request.user)

    return render(request, 'practician/profile.html', {'formUser': formUser, 'formTickets': formTickets, 'tickets': tickets})

def appointment(request, practician_id):
    practician = User.objects.get(id=practician_id)
    slots = practician.slots.filter(is_booked=False)

    return render(request, 'appointment/index.html', {'practician': practician, 'slots': slots})

def appointment_confirm(request, practician_id, slot_id):
    if request.method == 'POST':
        ticket = request.POST.get('ticket')

        slot = Slot.objects.get(id=slot_id)
        slot.is_booked = True
        slot.save()

        practician = User.objects.get(id=practician_id)

        appointment = Appointment()
        appointment.user_doctor = practician
        appointment.user_patient = request.user
        appointment.slot = slot
        appointment.ticket = Ticket.objects.get(id=ticket)
        appointment.save()

    return redirect('appointment', practician_id=practician_id)

@login_required
def practician_slots(request):
    if request.method == 'POST':
        form = SlotCreationForm(request.POST)
        if form.is_valid():
            slot = form.save(commit=False)
            slot.user = request.user
            slot.save()
    else:
        form = SlotCreationForm()

    return render(request, 'practician/slots.html', {'form': form})

@login_required
def patient_profile(request):
    appointments = Appointment.objects.all().filter(user_patient=request.user)

    return render(request, 'patient/index.html', {'appointments': appointments})