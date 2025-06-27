from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length= 100, verbose_name= "Nombre")
    
    #todas las imagenes de los proyectos de fguardan aqui las media que son las de los usuarios
   
    created = models.DateTimeField(auto_now_add= True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name= "fecha de modificacion")

    class Meta:
        verbose_name ="categoria"
        verbose_name_plural ="categorias"
        ordering =[ "-created"]

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length= 200, verbose_name= "Titulo")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name= "imagen", upload_to="blog", null= True, blank= True)
    author = models.ForeignKey(User, verbose_name="autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category,verbose_name="categorias", related_name='get_posts')
    
    #todas las imagenes de los proyectos de fguardan aqui las media que son las de los usuarios
   
    created = models.DateTimeField(auto_now_add= True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name= "fecha de modificacion")

    class Meta:
        verbose_name ="Post"
        verbose_name_plural ="Posts"
        ordering =[ "-created"]

    def __str__(self):
        return self.title