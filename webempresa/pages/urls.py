from django.urls import path
from . import views 

urlpatterns = [
    
    
    #coge el page_id como si fuese dinamico, es solo una cadena de caracteres pero a nosotros nos interesa un id(numerico)
    path('<int:page_id>/<slug:page_slug>/', views.page, name= 'page', ),
   
]
