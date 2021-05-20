from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .validators import validate_even

"""
Модель — это класс, описывающий определенную таблицу в базе данных, в частности набор имеющихся в ней полей. 
Отдельный экземпляр класса модели представляет отдельную запись таблицы, позволяет получать значения, хранящиеся
в полях записи, и заносить в них новые значения. Модель никак не привязана к конкретному формату базы данных.

Модель должна быть подклассом класса Model из модуля django.db.models. Отдельные поля модели объявляются в виде 
атрибутов класса, которым присваиваются экземпляры классов, представляющих поля разных типов и объявленных в том же
модуле. Параметры полей указываются в конструкторах классов полей в виде значений именованных параметров.

ПАРАМЕТРЫ, ПОДДЕРЖИВАЕМЫЕ ПОЛЯМИ ВСЕХ ТИПОВ:
- verbose_name - "человеческое” название поля, которое будет выводиться на вебстраницах. 
Если не указано, то будет выводиться имя поля;
- help_text - дополнительный поясняющий текст, выводимый на экран. По-умолчанию — пустая строка.
Содержащиеся в этом тексте специальные символы HTML не преобразуются в литералы и выводятся как есть. 
Это позволяет отформатировать поясняющий текст HTML-тегами;
- default - значение по умолчанию, записываемое в поле, если в него явно не было занесено никакого значения;
- unique - если True, то в текущее поле может быть занесено только уникальное в пределах таблицы значение 
(уникальное поле). При попытке занести значение, уже имеющееся в том же поле другой записи, будет возбуждено исключение
IntegrityError из модуля django.db. Если поле помечено как уникальное, по нему автоматически будет создан индекс. 
Поэтому явно задавать для него индекс не нужно;
- unique_for_date / unique_for_month / unique_for_year - если в этом параметре указать представленное в виде строки имя
поля даты (DateFieid) или даты и времени (DateTimeFieid), то текущее поле может хранить только значения, уникальные 
в пределах даты, которая хранится в указанном поле;
- null - если True, то поле в таблице базы данных может хранить значение null и, таким образом, являться необязательным 
к заполнению. Если False, то поле в таблице должно иметь какое-либо значение, хотя бы пустую строку.
У строковых и текстовых полей, даже обязательных к заполнению  (т. е. при их объявлении параметру null было присвоено 
значение False), вполне допустимое значение — пустая строка. Если сделать поля необязательными к заполнению, задав True 
для параметра null, то они вдобавок к этому могут хранить значение null. Оба значения фактически представляют отсутствие
каких-либо данных в поле, и эту ситуацию придется как-то обрабатывать. Поэтому, чтобы упростить обработку отсутствия 
значения в таком поле, его не стоит делать необязательным к заполнению. Параметр null затрагивает только поле таблицы, 
но не поведение Django. Даже если какое-то поле присвоением параметру значения True было помечено как необязательное, 
фреймворк по умолчанию все равно не позволит занести в него пустое значение;
- blank - если True, то Django позволит занести в поле пустое значение, тем самым сделав поле необязательным 
к заполнению, если False — не позволит. По-умолчанию — False. Параметр blank задает поведение самого фреймворка при 
выводе на экран вебформ и проверке введенных в них данных. Если этому параметру дано значение True, то Django позволит 
занести в поле пустое значение (например, для строкового поля — пустую строку), даже если это поле было помечено 
как обязательное к заполнению (параметру null было дано значение False);
- db_index - если True, то по текущему полю в таблице будет создан индекс, если False — не будет. По умолчанию — False;
- primary_key - если True, то текущее поле станет ключевым. Такое поле будет помечено как обязательное к заполнению 
и уникальное (параметру null неявно будет присвоено значение False, а параметру unique — True), и по нему будет
создан ключевой индекс. В модели может присутствовать только одно ключевое поле. Если ключевое поле в модели не было 
задано явно, сам фреймворк создаст в ней целочисленное автоинкрементное ключевое поле с именем id;
- editable - если True, то поле будет выводиться на экран в составе формы, если False - не будет (даже если явно создать 
его в форме). По умолчанию — True;
- db_column - имя поля таблицы в виде строки. Если не указано, то поле таблицы получит то же имя, что и поле модели;
"""


class Profile(models.Model):
    """ Расширение модели пользвателя """
    phone = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Bb(models.Model):
    """ Модель объявления """

    # по умолчанию любое поле обязательно к заполнению
    title = models.CharField(
        verbose_name='Товар',
        max_length=50,
    )
    """ Заголовк объявления с названием продаваемого товара """

    content = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True,
    )
    """ Текст объявления, описание товара """

    price = models.FloatField(
        verbose_name='Цена',
        null=True,
        blank=True,
        validators=[validate_even],
    )
    """ Цена """

    published = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
        db_index=True,
    )
    """ Дата публикации """
    # auto_now_add - при создании новой записи заносится в это поле текущие дата и время

    rubric = models.ForeignKey(
        'Rubric',
        verbose_name='Рубрика',
        null=True,
        on_delete=models.PROTECT,
    )
    """ Рубрика """
    # Первым параметром конструктору этого класса (ForeignKey) передается строка с именем класса
    # первичной модели, поскольку вторичная модель у нас объявлена раньше первичной.
    # on_delete=models.PROTECT - этого параметра запрещает каскадные удаления

    def title_and_price(self):
        """
        Метод для вычисления поля title_and_price.
        Достаточно объявить метод, не принимающий параметров и возвращающий
        нужное значение. Имя этого метода станет именем функционального поля.
        """
        if self.price:
            return '%s (%.2f)' % (self.title, self.price)
        else:
            return self.title
    # Для функционального поля допускается указать название, которое будет выводиться на веб-страницах.
    # Строку с названием нужно присвоить атрибуту short_description объекта метода, который реализует это поле
    # todo: поле не отображается
    title_and_price.short_description = 'Название и цена'

    def clean(self):
        """
        Может возникнуть необходимость проверить на корректность не значение одного
        поля, а всю модель (выполнить валидацию модели}. Для этого достаточно
        переопределить в классе модели метод clean().

        Если нужно вывести какое-либо сообщение об ошибке, относящейся не к определенному
        полю модели, а ко всей модели, то следует использовать в качестве ключа
        словаря, хранящего список ошибок, значение переменной NON_FIELD_ERRORS из
        модуля django.core.exceptions.
        """
        if not self.content:
            raise ValidationError(
                message='Укажите описание продаваемого товара.'
            )
        if self.price and self.price < 0:
            raise ValidationError(
                message='Цена товара не может быть отрицательной.'
            )

    class Meta:
        # название модели во множественном числе
        verbose_name_plural = 'Объявления'
        # название модели в единственном числе
        verbose_name = 'Объявление'
        # последовательность полей, по которым по умолчанию будет выполняться сортировка записей
        ordering = ('-published',)
        # последовательность имен полей, представленных в виде строк, которые должны
        # хранить уникальные в пределах таблицы комбинации значений. Можно указать несколько
        # подобных групп полей, объединив их в последовательность (кортеж кортежей)
        unique_together = ('title', 'published')


class Rubric(models.Model):
    """ Рубрика объявления """

    name = models.CharField(
        max_length=20,
        db_index=True,
        verbose_name='Название',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ('name',)
