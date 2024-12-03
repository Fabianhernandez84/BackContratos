from django.contrib import admin

# Register your models here.
from apps.empresas.models import Empresa


class EmpresaAdmin(admin.ModelAdmin):

    list_display=(
        'id',
        'nombre',
        'nit',
        'direccion',
        'contacto',
        'telefono',
        'email',
        'create_at',
        'modified_at',           
     
    )

admin.site.register(Empresa, EmpresaAdmin)