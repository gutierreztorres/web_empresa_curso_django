#crear mis propios template tags
from django import template
from pages.models import Page

#debemos registar el template fetpageslist en la libreria de tamplates
register = template.Library()

@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages

