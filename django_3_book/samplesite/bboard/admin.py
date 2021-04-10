from django.contrib import admin
from .models import Bb


class BbAdmin(admin.ModelAdmin):
    """ Класс редактора модели объявлений """
    # последовательность имен полей, которые должны выводиться в списке записей
    list_display = ('title', 'content', 'price', 'published')
    # последовательность имен полей, которые должны быть преобразованы в гиперссылки, ведущие на страницу правки записи
    list_display_links = ('title', 'content')
    # последовательность имен полей, по которым должна выпол няться фильтрация
    search_fields = ('title', 'content')


admin.site.register(Bb, BbAdmin)

