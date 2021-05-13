from django.urls import path
# noinspection PyUnresolvedReferences
from bboard.views import (
    index,
    by_rubric,
    BbCreateView,
    BbDetailView,
    BbRubricView,
    BbByRubricListView,
    BbAddView,
    BbEditView,
    BbDeleteView,
)
from .views import add_and_save


urlpatterns = [
    # path('add/', add_and_save, name='add'),
    path('add/', BbAddView.as_view(), name='add'),
    # через класс-контроллер
    # path(’add/', BbCreateView.as_view(model=Bb, template_name=’bboard/create.html’)),

    # угловые скобки помечают описание URL-параметра, языковая конструкция int задает
    # целочисленный тип этого параметра, a rubric id — имя параметра контроллера,
    # которому будет присвоено значение этого URL-параметра. Созданному маршруту мы
    # сопоставили контроллер-функцию by_rubric().

    # Получив запрос по интернет-адресу http://localhost:8000/bboard/2/, маршрутизатор
    # выделит путь bboard/2/, удалит из него префикс bboard и выяснит, что полученный путь
    # совпадает с первым маршрутом из приведенного ранее списка. После чего запустит контроллер
    # by rubric, передав ему в качестве параметра выделенный из интернет-адреса ключ рубрики 2

    # Имя маршрута указывается в именованном параметре name функции path()
    # Есть еще один способ передать какие-либо данные в контроллер. Для этого нужно объявить словарь Python,
    # создать в нем столько элементов, сколько нужно передать значений, присвоить передаваемые значения этим элементам
    # и передать полученный словарь функции path() в третьем параметре. Эти значения контроллер сможет получить также
    # через одноименные параметры. Вот пример передачи контроллеру-функции значения mode:
    # vals = {’mode’: ’index’}
    # urlpatterns = [
    #     path(’<int:rubric_id>/', by_rubric, vals),
    # ]
    path('<int:rubric_id>/', BbRubricView.as_view(), name='by_rubric'),
    # todo: вроде как отображение такое же как и у BbRubricView
    # path('<int:rubric_id>/', BbByRubricListView.as_view(), name='by_rubric'),

    # Корневой маршрут, указывающий на "корень” приложения bboard
    # с пустой строкой связываем функцию контроллера index() - samplesite.bboard.views.index
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('detail/<int:pk>/edit/', BbEditView.as_view(), name='edit'),
    path('detail/<int:pk>/delete/', BbDeleteView.as_view(), name='delete'),
    path('', index, name='index'),
]
