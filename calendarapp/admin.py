from django.contrib import admin
from calendarapp import models
from .models.linea_presupuesto import Line_Presupuesto


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    model = models.Event
    list_display = [
        'id', 'title', 'user', 'is_active', 'is_deleted', 'created_at',
        'updated_at'
    ]
    list_filter = ['is_active', 'is_deleted']
    search_fields = ['title']


@admin.register(models.EventMember)
class EventMemberAdmin(admin.ModelAdmin):
    model = models.EventMember
    list_display = ['id', 'event', 'user', 'created_at', 'updated_at']
    list_filter = ['event']




#@admin.register(models.linea_presupuesto)
class LineaPresupuestoAdmin(admin.ModelAdmin):
    model = Line_Presupuesto
    list_display = [ 'Proyecto', 'Codigo', 'Total', 'Ejecutado','En_Ejucucion','Saldo']
    list_filter = ['Proyecto','Codigo']

admin.site.register(Line_Presupuesto,LineaPresupuestoAdmin)