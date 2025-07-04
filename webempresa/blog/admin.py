from django.contrib import admin
from .models import Category,Post
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display=('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    #author es un modelo relacionado por tanto para buscar por el lo hacemos distinto y necesitamos hacer referencia al nombre del campo
    search_fields=('title','author__username','categories__name')
    date_hierarchy ='published'
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        return ", ".join ([c.name for c in obj.categories.all().order_by('name')])
    post_categories.short_description = 'Categorias'

admin.site.register(Category,CategoryAdmin)

admin.site.register(Post,PostAdmin)
