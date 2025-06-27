from .models import Link

#para crear un procesador de constexto
def ctx_dict(request):
    ctx={}
    links= Link.objects.all()
    for link in links:
        ctx[link.key]=link.url
    return ctx

#objetivo es que el diccionario extienda el contexto global de forma que podamos usar la clave test como una variable en cualquier template en context procesos en settings 