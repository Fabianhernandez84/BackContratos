from django.contrib import admin

# Register your models here.
from apps.terceros.models import Tercero


class TerceroAdmin(admin.ModelAdmin):

    list_display=(
        'id',
        'nombre',
        'cedula',
        'direccion',
        'contacto',
        'telefono',
        'email',
        'cedula',
        'create_at',
        'modified_at',           
     
    )

admin.site.register(Tercero, TerceroAdmin)