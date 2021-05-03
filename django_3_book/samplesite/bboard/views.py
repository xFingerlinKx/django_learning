from django.http import HttpResponseRedirect
from django.shortcuts import render, get_list_or_404
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
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


class BbDetailView(DetailView):
    """
    Форма объявления.

    Контроллер-класс Detailview наследует классы View, SingleObjectMixin и SingieObjectTemplateResponseMixin.
    Он ищет запись по полученным значениям ключа или слага, заносит ее в атрибут object
    (чтобы успешно работали наследуемые им примеси) и выводит на экран страницу с содержимым этой записи.
    """
    model = Bb

    # Компактность кода контроллера обусловлена в том числе и тем, что он следует
    # соглашениям. Так, в нем не указан путь к шаблону — значит, класс будет искать
    # шаблон со сформированным по умолчанию путем bboard\bb_detail.html.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BbByRubricListView(ListView):
    """
    Класс-контроллер. Наследует классы View, MultipleObjectMixin и MultipleObjectTemplateResponseMixin.
    Извлекает из модели набор записей, записывает его в атрибут object_list (чтобы успешно работали наследуемые
    им миксины) и выводит на экран страницу со списком записей.
    """
    template_name = 'bboard/by_rubric.html'
    context_object_name = 'bbs'

    def get_queryset(self):
        return Bb.objects.filter(rubric=self.kwargs['rubric_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['rubrics'] = Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(pk=self.kwargs['rubric_id'])
        return context


class BbRubricView(TemplateView):
    """
    Форма страницы с объявлениями в рубрике.

    Контроллер-класс Templateview наследует классы View, ContextMixin И TemplateResponseMixin.
    Он автоматически выполняет рендеринг шаблона и отправку ответа при получении запроса по методу GET.
    """
    template_name = 'bboard/by_rubric.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bbs'] = Bb.objects.filter(rubric=context['rubric_id'])
        context['rubrics'] = Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(pk=context['rubric_id'])
        return context


def by_rubric(request, rubric_id):
    """
    Функция-контроллер.
    todo: вместо нее используется класс-контроллер BbRubricView
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


class BbAddView(FormView):
    """
    Класс-контроллер, производный от FormMixin, ProcessFormView и TemplateResponseMixin, создает форму,
    выводит на экран страницу с этой формой, проверяет на корректность введенные данные и, в случае
    отрицательного результата проверки, выводит страницу с формой повторно. Нам остается только
    реализовать обработку корректных данных, переопределив метод form valid().
    """
    template_name = 'bboard/create.html'
    form_class = BbForm
    initial = {'price': 0.0}

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        """
        При написании этого класса мы столкнемся с проблемой. Чтобы после сохранения объявления сформировать
        интернет-адрес для перенаправления, нам нужно получить значение ключа рубрики, к которой относится
        добавленное объявление. Поэтому мы переопределили метод get_form(), в котором сохранили созданную
        форму в атрибуте object. После этого в коде метода get_success_url () без проблем
        сможем получить доступ к форме и занесенным в нее данным.
        """
        self.object = super().get_form(form_class)
        return self.object

    def get_success_url(self):
        return reverse(
            'by_rubric',
            kwargs={'rubric_id': self.object.cleaned_data['rubric'].pk}
        )


class BbCreateView(CreateView):
    """
    Форма создания объявления.

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


class BbEditView(UpdateView):
    """
    Контроллер UpdateView наследует от классов ProcessFormView, ModelFormMixin и SingleObjectTemplateResponseMixin.
    Он ищет запись по полученным ИЗ URL-параметра ключу или слагу, выводит страницу с формой для ее правки, проверяет
    и сохраняет исправленные данные.
    """
    model = Bb
    form_class = BbForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.get_object().id})


class BbDeleteView(DeleteView):
    """
    Удаление объявления.

    Контроллер UpdateView наследует от классов ProcessFormView, ModelFormMixin и SingleObjectTemplateResponseMixin.
    Он ищет запись по полученным ИЗ URL-параметра ключу или слагу, выводит страницу с формой для ее правки, проверяет
    и сохраняет исправленные данные.
    """
    model = Bb
    form_class = BbForm
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
