from django.template import Library
import women.views as views
from women.models import Category, TagsPost

register = Library()


@register.simple_tag(name='getcats')
def get_categories():
    cats = Category.objects.all()
    return cats


@register.inclusion_tag('women/includes/categories_list.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('women/includes/tag_postlist.html')
def show_tags():
    return {'tags': TagsPost.objects.all()}