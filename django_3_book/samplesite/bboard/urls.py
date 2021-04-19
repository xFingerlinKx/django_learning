from django.urls import path
# noinspection PyUnresolvedReferences
from bboard.views import index, by_rubric, BbCreateView


urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    # угловые скобки помечают описание URL-параметра, языковая конструкция int задает
    # целочисленный тип этого параметра, a rubric id — имя параметра контроллера,
    # которому будет присвоено значение этого URL-параметра. Созданному маршруту мы
    # сопоставили контроллер-функцию by_rubric().

    # Получив запрос по интернет-адресу http://localhost:8000/bboard/2/, маршрутизатор
    # выделит путь bboard/2/, удалит из него префикс bboard и выяснит, что полученный путь
    # совпадает с первым маршрутом из приведенного ранее списка. После чего запустит контроллер
    # by rubric, передав ему в качестве параметра выделенный из интернет-адреса ключ рубрики 2

    # Имя маршрута указывается в именованном параметре name функции path()
    path('<int:rubric>/', by_rubric, name='by_rubric'),
    # с пустой строкой связываем функцию контроллера index() - samplesite.bboard.views.index
    path('', index, name='index')
]
