from django.db import models

# Create your models here.
class Link(models.Model):
    #mapeamos los enlaces dentro de la memoria de la pagina usando la key y accederemos como un diccionario
    key= models.SlugField(verbose_name="nombre clave", unique=True, max_length=100)
    name=models.CharField(verbose_name="red social" , max_length=200)

    url =models.URLField(verbose_name="Enlace", null=True, blank= True, max_length=200)
    created = models.DateTimeField(auto_now_add= True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name= "fecha de modificacion")
    

    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"
        ordering=['name']

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
     #   return reverse("_detail", kwargs={"pk": self.pk})

