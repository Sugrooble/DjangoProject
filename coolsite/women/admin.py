from django.contrib import admin, messages
from women.models import Women, Category


class MarriedFilter(admin.SimpleListFilter):
    title = 'Статус женщины'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published', 'cat', 'count_symbols')
    list_display_links = ('id', 'title')
    ordering = ('time_create',)
    list_editable = ('is_published',)
    list_per_page = 5
    actions = ('set_published', 'set_draft')
    search_fields = ('title__startswith', )
    list_filter = (MarriedFilter, 'cat', 'is_published')

    @admin.display(description='Количество символов')
    def count_symbols(self, women: Women):
        return f'В статье {len(women.content)} символов.'

    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        return self.message_user(request, f'Опубликовано {count} записей.')

    @admin.action(description='Снять с публикации выбранные записи')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        return self.message_user(request, f'{count} записей снято с публикации!', messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


# admin.site.register(Women, WomenAdmin) #Аналогично декоратору
