from django.shortcuts import render

from . models import Bb, Rubric

"""
Контроллер Django — это код, запускаемый при обращении по интернет-адресу
определенного формата и в ответ выводящий на экран определенную веб-страницу.

Любой контроллер-функция в качестве единственного обязательного параметра
принимает экземпляр класса HttpRequest, хранящий различные сведения о полученном запросе: 
запрашиваемый интернет-адрес, данные, полученные от посетителя, служебную информацию от самого 
веб-обозревателя и пр. По традиции этот параметр называется request. В нашем случае мы его никак не используем.
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


def by_rubric(request, rubric_id):
    """
    В объявление функции мы добавили параметр rubric id — именно ему будет присвоено
    значение URL-параметра, выбранное из интернет-адреса. В состав контекста шаблона
    поместили список объявлений, отфильтрованных по полю внешнего ключа rubric_id,
    список всех рубрик и текущую рубрику (она нужна нам, чтобы вывести на странице ее название).
    """
    bbs = Bb.objects.filter(rubric_id=rubric_id)
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
