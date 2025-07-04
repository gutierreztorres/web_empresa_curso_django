from django.contrib import admin
from .models import Link
# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    #para dar o quitar permisos solo a algunos campos
    def get_readonly_fields(self, request, obj =None):
        if request.user.groups.filter(name="Personal").exists():

            return ('created', 'updated','key','name')
        else:
             return ('created', 'updated')

    
admin.site.register(Link,LinkAdmin)




