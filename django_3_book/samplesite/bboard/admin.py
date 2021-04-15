from django.contrib import admin
from .models import Bb
from .models import Rubric


class BbAdmin(admin.ModelAdmin):
    """ Класс редактора модели объявлений для админки """
    # последовательность имен полей, которые должны выводиться в списке записей
    list_display = ('title', 'content', 'price', 'published', 'rubric_id')
    # последовательность имен полей, которые должны быть преобразованы в гиперссылки, ведущие на страницу правки записи
    list_display_links = ('title', 'content', 'rubric_id')
    # последовательность имен полей, по которым должна выполняться фильтрация ???
    search_fields = ('title', 'content', 'rubric_id')


# class RubricAdmin(admin.ModelAdmin):
#     """ Класс редактора модели рубрик для админки """
#     list_display = ('name',)
#     list_display_links = ('name',)
#     search_fields = ('name',)


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
