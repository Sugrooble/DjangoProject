from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string

from women.models import Women, Category, TagsPost

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_post'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]


def main_page(request):
    # t = render_to_string('women/index.html') # Аналогично функции render
    # return HttpResponse(t)
    posts = Women.published.all().select_related('cat')
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
    posts = Women.published.filter(cat_id=category.pk).select_related('cat')

    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk
    }
    return render(request, 'women/index.html', data)


def categories_by_slug(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk).select_related('cat')

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


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagsPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED).select_related('cat')

    data = {
        'title': f'Статьи по тэгу {tag.tag}',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0
    }
    return render(request, 'women/index.html', data)


def add_post(request):
    return HttpResponse(f'<h1>Добавить новую статью</h1>')


def contact(request):
    return HttpResponse(f'<h1>Обратная связь</h1>')


def login(request):
    return HttpResponse(f'<h1>Авторизация</h1>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
