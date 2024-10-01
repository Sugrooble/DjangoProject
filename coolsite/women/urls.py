from django.urls import path, re_path, register_converter
from women.views import *
from women.converters import FourDigitsConverter

register_converter(FourDigitsConverter, 'year4')

urlpatterns = [
    path('', main_page, name='home'),
    path('cats/<int:cat_id>/', categories, name='cats_id'),
    path('cats/<slug:cat_slug>/', categories_by_slug, name='cats_slug'),
    path('archive/<year4:year>/', archive)
]
