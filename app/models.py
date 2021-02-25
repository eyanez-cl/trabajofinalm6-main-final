from django.db import models

# Create your models here.



class Administradores(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=254)
    clave = models.CharField(max_length=50)
    
class Pacientes(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=200)
    clave = models.CharField(max_length=50, default='123456')
    rut = models.CharField(max_length=10)
    edad = models.IntegerField()
    fecha = models.DateField()
    direccion = models.CharField(max_length=150)
    ocupacion = models.CharField(max_length=150, default='influencer')
    telefono = models.CharField(max_length=20)
    foto = models.CharField(max_length=65535, default='complete info')
    resumen= models.TextField(default='complete la info')
    educacion=models.TextField(default='complete la info')
    historial = models.TextField(default='complete la info')
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return self.nombre
    
   
    
class Examenes(models.Model):
    nombre = models.CharField(max_length=50)
    valor = models.CharField(max_length=50)
    fecha = models.DateField()
    observaciones = models.CharField(max_length=250)
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['id']

