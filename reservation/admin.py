from django.contrib import admin
from .models import Office, Room, Employee


# Register your models here.
class OfficeAdmin(admin.ModelAdmin):
    list_display = ("office_name", "address", "number_of_rooms")


class RoomAdmin(admin.ModelAdmin):
    list_display = ("room_number", "number_seats")


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "room_number")


admin.site.register(Office, OfficeAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Employee, EmployeeAdmin)
