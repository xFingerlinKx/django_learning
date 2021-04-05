from django.urls import path
# noinspection PyUnresolvedReferences
from bboard.views import index


urlpatterns = [
    # с пустой строкой связываем функцию контроллера index() - samplesite.bboard.views.index
    path('', index)
]
