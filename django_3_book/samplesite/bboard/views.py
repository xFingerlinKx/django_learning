from django.http import HttpResponse

from . models import Bb

"""
Контроллер Django — это код, запускаемый при обращении по интернет-адресу
определенного формата и в ответ выводящий на экран определенную веб-страницу.

Любой контроллер-функция в качестве единственного обязательного параметра
принимает экземпляр класса HttpRequest, хранящий различные сведения о полученном запросе: 
запрашиваемый интернет-адрес, данные, полученные от посетителя, служебную информацию от самого 
веб-обозревателя и пр. По традиции этот параметр называется request. В нашем случае мы его никак не используем.
"""


def index(request):
    title_str = 'Список объявлений\r\n\r\n\r\n'
    for bb in Bb.objects.order_by('published'):
        title_str += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    return HttpResponse(title_str, content_type='text/plain; charset=utf-8')
