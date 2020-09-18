from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Negocio(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	id_negocio = models.AutoField(primary_key=True)
	direccion = models.CharField(max_length=25)
	nombre_local= models.CharField(max_length=20)
	nom_responsable = models.CharField(max_length=20)
	estancia = models.DecimalField(max_digits=25,decimal_places=0, default=30)
	turno = models.DecimalField(max_digits=25,decimal_places=0, default=6)

	def __str__(self):
		return f'{self.nombre_local}'

class Visitas (models.Model): 
	celular = models.DecimalField(max_digits= 20,decimal_places=0,default=1)
	fecha_visita = models.DateField(auto_now=True)
	negocio = models.ForeignKey(Negocio, on_delete=models.PROTECT,default=1)

	def __str__(self):
		return f'{self.celular}-{self.fecha_visita}'



class Positivo(models.Model):
	fecha_test = models.DateField(null=False,blank=False)
	celular = models.DecimalField(max_digits= 20,decimal_places=0)

	def __str__(self):
		return f'{self.celular}'

class Aviso(models.Model):
	negocio = models.ForeignKey(Negocio, on_delete= models.CASCADE)
	visitante = models.ForeignKey(Positivo, on_delete= models.PROTECT)
	fecha = models.DateField(auto_now=True)










#TIME_CHOICES = ( 
#    ("H", "HORAS"), 
#    ("M", "MINUTOS"), 
#	)


#

#class Negocio(models.Model): 
#	perma_um = models.CharField( 
#		max_length = 7, 
#		choices = TIME_CHOICES, 
#		default = 'm'
#		) 