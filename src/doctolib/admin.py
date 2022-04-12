from django.contrib import admin
from .models import *

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    pass
admin.site.register(Ticket, TicketAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff',)
    pass
admin.site.register(User, UserAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'confirmed', 'slot')
    pass
admin.site.register(Appointment, AppointmentAdmin)

class GeoLocationAdmin(admin.ModelAdmin):
    list_display = ('id',)
    pass
admin.site.register(GeoLocation, GeoLocationAdmin)

class SlotAdmin(admin.ModelAdmin):
    list_display = ('id',)
    pass
admin.site.register(Slot, SlotAdmin)