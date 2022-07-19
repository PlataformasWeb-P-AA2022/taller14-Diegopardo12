from django.contrib import admin

from administrativo.models import Propietario, Departamento

class PropietarioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'edad', 'nacionalidad')
    search_fields = ('nombre', 'nacionalidad')

admin.site.register(Propietario, PropietarioAdmin)


class DepartamentoAdmin(admin.ModelAdmin):

    list_display = ('costo_dep', 'num_cuartos', 'num_banos', 'valor_ali','propietario')

    raw_id_fields = ('propietario',)

admin.site.register(Departamento, DepartamentoAdmin)
