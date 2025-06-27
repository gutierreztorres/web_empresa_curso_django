from django.shortcuts import render,HttpResponse, get_object_or_404
from .models import Post, Category

# Create your views here.
def blog (request):
    posts= Post.objects.all()
    return render(request,"blog/blog.html", {'posts':posts})

def category(request, category_id):
    category= get_object_or_404(Category, id=category_id)
    #forma rudimentaria de crear la vista por categorias luego tendriamos que pasarle el post al render igual que la category
   # posts= Post.objects.filter(categories =category)
    #forma de hacerlo facil en el for de category.html pero solo podemos tener una relacion
    return render(request,"blog/category.html", {'category':category})


