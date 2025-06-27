from django.db import models
#importamos el ckeditos
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    #mapeamos los enlaces dentro de la memoria de la pagina usando la key y accederemos como un diccionario
    
    title=models.CharField(verbose_name="titulo" , max_length=200)
    #cambiamos el tipo de campo a texto enriquecido de la clase ckeditor
    content = RichTextField(verbose_name="contenido")
    #para ordenar haremos cambios en la ordenacion y en el administrador y migraremos. 0 es el 1º
    order = models.SmallIntegerField(verbose_name="orden", default= 0)
    created = models.DateTimeField(auto_now_add= True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name= "fecha de modificacion")
    

    class Meta:
        verbose_name = ("Página")
        verbose_name_plural = ("Páginas")
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    


