from django.forms import ModelForm, modelform_factory, DecimalField
from django.forms.widgets import Select


from .models import Bb


# !!! Есть еще третьй способ создания формы - путем полного объявления
# указанный вариант позволяет добавлять новые поля на форму, устанавливать размер значений, валидаторы, обязательность

# создание формы для объявления с использованием класса
class BbForm(ModelForm):
    """ Форма, связанная с моделью Bb """
    class Meta:
        # класс модель, с которой связана форма
        model = Bb
        # последовательность полей, которые должны присутствовать в форме
        fields = ('title', 'content', 'price', 'rubric')
        labels = {'title': 'Название товара'}
        help_texts = {'rubric': 'Не забудьте выбрать рубрику'}
        field_classes = {'price': DecimalField}
        widgets = {'rubric': Select(attrs={'size': 1})}

# создание формы для объявления с использованием фабрики классов modelform_factory()
# BbForm = modelform_factory(
#     model=Bb,
#     fields=('title', 'content', 'price', 'rubric'),
#     labels={'title': 'Название товара'},
#     help_texts={'rubric': 'Не забудьте выбрать рубрику'},
#     field_classes={'price': DecimalField},
#     widgets={'rubric': Select(attrs={'size': 3})}
# )
