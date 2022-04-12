from django.contrib import admin
from .models import Ticket
from .models import User

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    pass
admin.site.register(Ticket, TicketAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff',)
    pass
admin.site.register(User, UserAdmin)