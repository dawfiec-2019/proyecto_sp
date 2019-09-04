from django.db import models

# Create your models here.


class Asableista(models.Model):
    id_asambleista = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    partido = models.CharField(max_length=35)



class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    contrasena = models.CharField(max_length=10)
    nombreUsuario = models.CharField(max_length=10)


class Ley(models.Model):
    id_ley= models.AutoField(primary_key=True)
    nombre_oficial = models.CharField(max_length=35)
    nombre_publico = models.CharField(max_length=35)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=100)

class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    correo = models.CharField(max_length=35)
    ruta_imagen = models.CharField(max_length=35)


class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=35)
    fecha = models.DateField()

class ComentarioLey(models.Model):
    id_ley = models.ForeignKey(Ley,  null=False, blank=False, on_delete=models.CASCADE)
    id_comentario = models.ForeignKey(Comentario, null=False, blank=False, on_delete=models.CASCADE)


class Voto(models.Model):
    id_ley = models.ForeignKey(Ley, null=False, blank=False, on_delete=models.CASCADE)
    id_asambleista = models.ForeignKey(Asableista, null=False, blank=False, on_delete=models.CASCADE)
    voto = models.CharField(max_length=35)

