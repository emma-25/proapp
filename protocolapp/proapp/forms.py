from django.forms import ModelForm
from proapp.models import Positivo, Visitas, Negocio
#
class PositivoForm (ModelForm):
	class Meta:
		model = Positivo 
		fields = ('fecha_test','celular',)
        

class VisitaForm (ModelForm):
	class Meta:
		model = Visitas
		fields = ('celular','negocio')


class NegocioForm(ModelForm):
	class Meta:
		model = Negocio
		fields = ('nombre_local','direccion','nom_responsable','estancia','turno')