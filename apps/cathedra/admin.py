from django.contrib import admin

from cathedra.models import Lector, Room, Position, Science


admin.site.register(Lector)
admin.site.register(Room)
admin.site.register(Position)
admin.site.register(Science)
