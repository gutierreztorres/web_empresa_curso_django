from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    contact_form= ContactForm()
    #SI DETECTAMOS QUE LO QUE ENVIA ES UN FORMULARIO (SI NO SERIA GET) ENVIAMOS LA PLANTILLA CON LOS DATOS
    if request.method == 'POST':
        contact_form= ContactForm(data= request.POST)
        if contact_form.is_valid():
            name= request.POST.get('name','')
            email= request.POST.get('email','')
            content= request.POST.get('content','')
            #ENVIAMOS CORREO Y REDIRECCIONAMOS AL CORREO DE PRUEBA CON LA CONFIGURACION DE SETTING
            email= EmailMessage(
                "Asunto: nuevo mensaje",
               "De {} <{}>\n\nEscribio:\n\n{}".format(name,email,content) ,
                {"no-contestar@inbox.mailtrap.io"},
                ['andrea-msn@hotmail.com'],
                reply_to=[email]
            )
           
            email.send()
            return redirect(reverse('contact') + '?ok')
            

    
        return render(request,"contact/contact.html", {'form':contact_form})