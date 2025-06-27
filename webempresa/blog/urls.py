from django.urls import path
from . import views 

urlpatterns = [
    
    path('',views.blog, name="blog"),
    #coge el category_id como si fuese dinamico, es solo una cadena de caracteres pero a nosotros nos interesa un id(numerico)
    path('category/<int:category_id>', views.category, name= 'category'),
   
]
