from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    sinopsis = models.TextField()
    estreno = models.DateField()
    imagen = models.ImageField(upload_to='imagenes/')

    def __str__(self):
        return self.titulo

class Reseña(models.Model):
    pelicula = models.ForeignKey('Pelicula', on_delete=models.CASCADE, related_name='reseñas')
    usuario = models.CharField(max_length=100)
    comentario = models.TextField()
    calificacion = models.PositiveIntegerField()  # Valor del 1 al 10
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reseña de {self.usuario} para {self.pelicula.titulo}'

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Mensaje de {self.nombre} - {self.email}'