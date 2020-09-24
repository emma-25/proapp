from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Negocio(models.Model):
	usuario = models.OneToOneField(User,on_delete=models.PROTECT,unique=True, default=1)
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
	fecha_visita = models.DateTimeField(auto_now_add=True, editable=False)
	negocio = models.ForeignKey(Negocio, on_delete=models.PROTECT,default=1)
	empleado = models.BooleanField(default=False)


	def __str__(self):
		return f'{self.celular}-{self.fecha_visita}'



class Positivo(models.Model):
	fecha_test = models.DateField(null=False,blank=False)
	celular = models.DecimalField(max_digits= 20,decimal_places=0)

	def __str__(self):
		return f'{self.celular}'

class Alerta(models.Model):
	negocio = models.ForeignKey(Negocio, on_delete= models.CASCADE)
	positivo = models.ForeignKey(Positivo, on_delete= models.PROTECT)
	fecha = models.DateField(auto_now=True)

	def __str__(self):
		return f'En {self.negocio} concurrió {self.positivo}'



class Cercano(models.Model):
	aviso = models.ForeignKey(Alerta, on_delete= models.CASCADE)
	tel_cercano = models.DecimalField(max_digits=20,decimal_places=0)
	avisado = models.BooleanField(default=False)

	def __str__(self):
		return f'La persona {self.tel_cercano} estuvo en contacto con {self.aviso.positivo}'













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