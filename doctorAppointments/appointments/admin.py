from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    readonly_fields=('created_at')

admin.site.register(Booking, BookingAdmin)
