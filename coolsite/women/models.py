from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_cat_by_slug', kwargs={'cat_slug': self.slug})


class TagsPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tags', kwargs={'tag_slug': self.slug})


class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = (0, 'Черновик')
        PUBLISHED = (1, 'Опубликовано')

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True, verbose_name='Содержание статьи')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name='Статус')
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')
    tags = models.ManyToManyField(TagsPost, blank=True, related_name='tags', verbose_name='Теги')
    husband = models.OneToOneField('Husband', on_delete=models.SET_NULL, blank=True, null=True, related_name='woman', verbose_name='Муж') # Если модель, с которой связан внешний ключ, объявлена после текущей модели, её название можно передать в виде строки

    objects = models.Manager() # Если в классе объявлен кастомный менеджер записей, базовый objects становится недоступен и его нужно объявить явно
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('show_post_by_slug', kwargs={'post_slug': self.slug})


class Husband(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    marriage_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name
