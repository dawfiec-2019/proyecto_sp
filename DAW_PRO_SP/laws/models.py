from django.db import models

# Create your models here.


class Asambleista(models.Model):
    id_asambleista = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    partido = models.CharField(max_length=100)

class Ley(models.Model):
    id_ley= models.CharField(max_length=30,primary_key=True)
    nombre_oficial = models.CharField(max_length=300)
    nombre_publico = models.CharField(max_length=300)
    fecha = models.CharField(max_length=35)
    descripcion = models.CharField(max_length=300)

class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    ruta_imagen = models.CharField(max_length=100)


class Usuario(models.Model):
    id_persona = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.CASCADE)
    id_usuario = models.AutoField(primary_key=True)
    contrasena = models.CharField(max_length=10)
    usuario_nombre = models.CharField(max_length=20)
    

class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=35)
    fecha = models.CharField(max_length=35)

class ComentarioLey(models.Model):
    id_ley = models.ForeignKey(Ley,null=False, blank=False, on_delete=models.CASCADE)
    id_comentario = models.ForeignKey(Comentario, null=False, blank=False, on_delete=models.CASCADE)
    class Meta:
        unique_together=('id_ley','id_comentario')

class Voto(models.Model):
    id_ley = models.ForeignKey(Ley, null=False, blank=False, on_delete=models.CASCADE)
    id_asambleista = models.ForeignKey(Asambleista, null=False, blank=False, on_delete=models.CASCADE)
    voto = models.CharField(max_length=35)
    class Meta:
        unique_together=('id_ley','id_asambleista')


