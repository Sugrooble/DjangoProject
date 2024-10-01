from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse


def main_page(request):
    return HttpResponse('Страница приложения Women.')


def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    if 'music' in cat_slug and cat_slug != 'music':
        uri = reverse('cats_slug', args=('music',))
        return redirect(uri)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>')


def archive(request, year):
    if int(year) > 2024:
        # return redirect('home') # Редирект с кодом 302 (на временный урл)
        # return redirect('home', permanent=True) # Редирект с кодом 301 (на постоянный урл)
        raise Http404()

    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')