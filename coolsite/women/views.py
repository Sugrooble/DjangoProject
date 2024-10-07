from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string

from women.models import Women, Category

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_post'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Линдси Лохан', 'content': 'Биография Линдси Лохан', 'is_published': True},
]

cats_db = [
    {'id': 1, 'cat_name': 'Актрисы'},
    {'id': 2, 'cat_name': 'Певицы'},
    {'id': 3, 'cat_name': 'Спортсменки'},
]


def main_page(request):
    # t = render_to_string('women/index.html') # Аналогично функции render
    # return HttpResponse(t)
    posts = Women.published.all()
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0
    }
    return render(request, 'women/index.html', data)


def about(request):
    # t = render_to_string('women/index.html') # Аналогично функции render
    # return HttpResponse(t)
    data = {
        'title': 'О сайте',
        'menu': menu,
    }
    return render(request, 'women/about.html', context=data)


def categories(request, cat_id):
    category = get_object_or_404(Category, pk=cat_id)
    posts = Women.published.filter(cat_id=category.pk)

    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk
    }
    return render(request, 'women/index.html', data)


def categories_by_slug(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk)

    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk
    }
    return render(request, 'women/index.html', data)


def archive(request, year):
    if int(year) > 2024:
        # return redirect('home') # Редирект с кодом 302 (на временный урл)
        # return redirect('home', permanent=True) # Редирект с кодом 301 (на постоянный урл)
        raise Http404()

    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def show_post(request, post_id):
    post = get_object_or_404(Women, pk=post_id)
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'post': post,
        'cat_selected': 1
    }
    return render(request, 'women/post.html', data)


def show_post_by_slug(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'post': post,
        'cat_selected': 1
    }
    return render(request, 'women/post.html', data)


def add_post(request):
    return HttpResponse(f'<h1>Добавить новую статью</h1>')


def contact(request):
    return HttpResponse(f'<h1>Обратная связь</h1>')


def login(request):
    return HttpResponse(f'<h1>Авторизация</h1>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
