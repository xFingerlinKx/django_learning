"""samplesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

"""
Path в качестве параметров принимает строку с шаблонным путем и ссылку на контроллер-функцию
В качестве второго параметра функции path () также можно передать список маршрутов уровня приложения.
В таком случае маршрутизатор, найдя совпадение, удалит из реального пути его
начальную часть (префикс), совпавшую с шаблонным путем, и приступит к просмотру маршрутов
из вложенного списка, используя для сравнения реальный путь уже без префикса.

Вложенный список маршрутов, указываемый во втором параметре функции path (),
должен представлять собой результат, возвращенный функцией include () из модуля django.urls. 
В качестве единственного параметра эта функция принимает строку
с путем к модулю, где записан вложенный список маршрутов.

Как только наш сайт получит запрос с интернет-адресом http://localhost:8000/bboard/, 
маршрутизатор обнаружит, что присутствующий в нем путь совпадаетс шаблонным путем bboard/, 
записанным в первом маршруте из листинга 1.5. Он удалит из реального пути префикс, 
соответствующий шаблонному пути, и получит новый путь — пустую строку. Этот путь совпадет с 
единственным маршрутом из вложенного списка (см. листинг 1.4), в результате чего запустится записанный
в этом маршруте контроллер-функция index (), и на экране появится уже знакомое нам текстовое сообщение.
"""


urlpatterns = [
    path('bboard/', include('bboard.urls')),
    path('admin/', admin.site.urls),
]
