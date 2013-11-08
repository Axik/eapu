from django.contrib import admin

from cathedra.models import Lector, Room, Position, Science, Aspirant, Technician


admin.site.register(Lector)
admin.site.register(Aspirant)
admin.site.register(Technician)
admin.site.register(Room)
admin.site.register(Position)
admin.site.register(Science)
