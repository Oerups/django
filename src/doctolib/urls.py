"""doctolib URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register, name='register'),
    path('practician/profile/', practician_profile, name='practician_profile'),
    path('patient/profile/', patient_profile, name='patient_profile'),
    path('practician/tickets/', practician_tickets, name='practician_tickets'),
    path('practician/', practician, name='practician'),
    path('appointment/practician/<practician_id>', appointment, name='appointment'),
    path('appointment/practician/<practician_id>/slot/<slot_id>', appointment_confirm, name='appointment_confirm'),
    path('accounts/register/practician', register_practician, name='register_practician'),
    path('practician/slots', practician_slots, name='practician_slots'),
]

