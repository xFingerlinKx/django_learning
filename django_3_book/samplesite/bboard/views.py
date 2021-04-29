from django.http import HttpResponseRedirect
from django.shortcuts import render, get_list_or_404
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse

from . models import Bb, Rubric
from .forms import BbForm

"""
Контроллер Django — это код, запускаемый при обращении по интернет-адресу
определенного формата и в ответ выводящий на экран определенную веб-страницу.

Любой контроллер-функция в качестве единственного обязательного параметра
принимает экземпляр класса HttpRequest, хранящий различные сведения о полученном запросе: 
запрашиваемый интернет-адрес, данные, полученные от посетителя, служебную информацию от самого 
веб-обозревателя и пр. По традиции этот параметр называется request. В нашем случае мы его никак не используем.

Контроллер-функция должен возвращать в качестве результата экземпляр класса HttpResponse, Также объявленного в модуле 
django.http, или какого-либо из его подклассов. Этот экземпляр класса представляет ответ, отсылаемый клиенту 
(веб-страница, обычный текстовый документ, файл, данные в формате JSON, перенаправление или сообщение об ошибке).
"""


class BbCreateView(CreateView):
    """
    Класс-контроллер.

    Базовый класс "знает", как создать форму, вывести на экран страницу с применением
    указанного шаблона, получить занесенные в форму данные, проверить их, сохранить в
    новой записи модели и перенаправить пользователя в случае успеха на заданный интернет-адрес.
    """
    # путь к файлу шаблона, создающего страницу с формой
    template_name = 'bboard/create.html'
    # ссылка на класс формы, связанной с моделью
    form_class = BbForm
    # интернет-адрес для перенаправления после успешного сохранения данных
    # (в нашем случае это адрес главной страницы)
    # Функция reverse_lazy() принимает имя маршрута и значения всех входящих в маршрут URL-параметров
    # (если они там есть). Результатом станет готовый интернет-адрес
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        """
        Поскольку на каждой странице сайта должен выводиться перечень рубрик, мы
        переопределили метод get_context_data(), формирующий контекст шаблона. В теле
        метода получаем контекст шаблона от метода базового класса, добавляем в него
        список рубрик и, наконец, возвращаем его в качестве результата.
        """
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    return render(
        request=request,
        template_name='bboard/index.html',
        context={
            'bbs': bbs,
            'rubrics': rubrics,
        }
    )


def by_rubric(request, rubric_id):
    """
    Ввыводит страницу с объявлениями, относящимися к выбранной посетителем рубрике.

    В объявление функции мы добавили параметр rubric_id — именно ему будет присвоено
    значение URL-параметра, выбранное из интернет-адреса. В состав контекста шаблона
    поместили список объявлений, отфильтрованных по полю внешнего ключа rubric,
    список всех рубрик и текущую рубрику (она нужна нам, чтобы вывести на странице ее название).
    """
    bbs = get_list_or_404(Bb, rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'bbs': bbs,
        'rubrics': rubrics,
        'current_rubric': current_rubric,
    }
    return render(
        request=request,
        template_name='bboard/by_rubric.html',
        context=context
    )


def add(request):
    """
    Функция-контроллер, которая создает форму и выводит на экран страницу добавленя объявления.

    :param request: экземпляр класса HttpRequest
    :return: экземпляр класса HttpResponse
    """
    bbf = BbForm()
    context = {'form': bbf}
    return render(request=request, template_name='bboard/create.html', context=context)


def add_and_save(request):
    """ Сохраняет новое объявление в БД """
    if request.method == 'POST':
        bbf = BbForm(request.POST)
        if bbf.is_valid():
            bbf.save()
            return HttpResponseRedirect(
                reverse(
                    viewname='by_rubric',
                    kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}
                )
            )
        else:
            context = {'form': bbf}
            return render(request, 'bboard/create.html', context)
    else:
        bbf = BbForm()
        context = {'form': bbf}
        return render(request, 'bboard/create.html', context)
