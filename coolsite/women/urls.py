from django.urls import path, re_path, register_converter
from women import views
from women.converters import FourDigitsConverter

register_converter(FourDigitsConverter, 'year4')

urlpatterns = [
    path('', views.main_page, name='home'),
    path('about/', views.about, name='about'),
    path('cats/<int:cat_id>/', views.categories, name='cats_id'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats_slug'),
    path('archive/<year4:year>/', views.archive, name='archive')
]
