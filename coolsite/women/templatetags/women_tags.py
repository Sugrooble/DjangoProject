from django.db.models import Count
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
    cats = cats = Category.objects.annotate(Count("name")).filter(posts__gt=0)
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('women/includes/tag_postlist.html')
def show_tags():
    return {'tags': TagsPost.objects.annotate(Count("id")).filter(tags__gt=0)}