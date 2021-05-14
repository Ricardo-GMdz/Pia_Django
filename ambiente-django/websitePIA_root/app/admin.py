from django.contrib import admin
from .models import Estanteria, Lockers, Muebles, Cajas

# Register your models here.
admin.site.register(Estanteria)
admin.site.register(Lockers)
admin.site.register(Muebles)
admin.site.register(Cajas)
