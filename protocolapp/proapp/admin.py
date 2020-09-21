from django.contrib import admin
from proapp.models import Visitas,Positivo, Negocio
# Register your models here.


class VisitasAdmin(admin.ModelAdmin):
	pass

class PositivoAdmin(admin.ModelAdmin):
	pass

class NegocioAdmin(admin.ModelAdmin):
	pass

class AlertaAdmin(admin.ModelAdmin):
	pass

class CercanoAdmin(admin.ModelAdmin):
	pass



admin.site.register(Positivo,PositivoAdmin)
admin.site.register(Visitas, VisitasAdmin)
admin.site.register(Negocio, NegocioAdmin)
admin.site.register(Alerta, AlertaoAdmin)
admin.site.register(Cercano,CercanoAdmin)
