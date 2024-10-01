from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Линдси Лохан', 'content': 'Биография Линдси Лохан', 'is_published': True},
]


def main_page(request):
    # t = render_to_string('women/index.html') # Аналогично функции render
    # return HttpResponse(t)
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db
    }
    return render(request, 'women/index.html', data)


def about(request):
    # t = render_to_string('women/index.html') # Аналогично функции render
    # return HttpResponse(t)
    data = {
        'title': 'О сайте',
        'menu': menu
    }
    return render(request, 'women/about.html', context=data)


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