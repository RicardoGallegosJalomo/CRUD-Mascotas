from django.db import models

class Personas(models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 30)
	apellido = models.CharField(max_length = 30)
	email = models.EmailField()
	Mascota = models.CharField(max_length= 30)

	def __str__(self):
		cadena = self. nombre + self.apellido + self.email + self.Mascota
		return cadena

class Mascota(models.Model):
	id= models.AutoField(primary_key = True)
	nombre = models.CharField(max_length=30)
	edad = models.IntegerField()
	peso = models.FloatField()
	personas = models.ForeignKey(Personas, on_delete = models.CASCADE)

	def __str__(self):
		cadenam = self. nombre + str(self.edad) + str(self.peso)
		return cadenam
