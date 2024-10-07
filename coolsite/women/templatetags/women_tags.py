from django.template import Library
import women.views as views
from women.models import Category

register = Library()


@register.simple_tag(name='getcats')
def get_categories():
    cats = Category.objects.all()
    return cats


@register.inclusion_tag('women/includes/categories_list.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}