from django.forms import ModelForm


from .models import Bb


class BbForm(ModelForm):
    """ Форма, связанная с моделью Bb """
    class Meta:
        # класс модель, с которой связана форма
        model = Bb
        # последовательность полей, которые должны присутствовать в форме
        fields = ('title', 'content', 'price', 'rubric_id')
