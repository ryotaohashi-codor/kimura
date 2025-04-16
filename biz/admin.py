from django.contrib import admin
from .models import Customer, Driver, Project, Delivery

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    search_fields = ('name', 'email')
    list_filter = ('name',)

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'license_number')
    search_fields = ('name', 'license_number')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer', 'start_date', 'end_date')
    search_fields = ('title', 'customer__name')
    list_filter = ('start_date', 'end_date')
    date_hierarchy = 'start_date'

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('project', 'driver', 'delivery_date', 'status')
    list_filter = ('status', 'delivery_date')
    search_fields = ('project__title', 'driver__name')
    date_hierarchy = 'delivery_date'