from django.contrib import admin
from .models import *


class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'age', 'created_at')
    list_display_links = ('id', 'last_name')
    search_fields = ('first_name', 'last_name', 'phone', 'age')


class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', '_clients', 'phone', 'potok', 'room', 'status')
    list_display_links = ('id', '_clients')
    search_fields = ('id', '_clients', 'phone', 'potok', 'room', 'status')

    def _clients(self, row):
        return ', '.join([x.last_name for x in row.clients.all()])


class DivisionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'photo_passport', 'phone', 'division')
    list_display_links = ('id', )
    search_fields = ('id', )


admin.site.register(Record)
admin.site.register(Tasks, TasksAdmin)
admin.site.register(Clients, ClientsAdmin)
admin.site.register(Divisions, DivisionsAdmin)
admin.site.register(Staff, StaffAdmin)
