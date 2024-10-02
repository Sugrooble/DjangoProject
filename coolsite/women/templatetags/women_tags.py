from django.template import Library
import women.views as views

register = Library()


@register.simple_tag(name='getcats')
def get_categories():
    return views.cats_db


@register.inclusion_tag('women/includes/categories_list.html')
def show_categories(cat_selected=0):
    cats = views.cats_db
    return {'cats': cats, 'cat_selected': cat_selected}