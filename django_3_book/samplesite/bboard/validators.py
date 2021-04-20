from django.core.exceptions import ValidationError


def validate_even(val):
    """
    Валидатор для поля типа FloatField.
    Число должно быть четным.
    """
    if val % 2 != 0:
        raise ValidationError(
            message=f'Число {val} нечетное',
            code='odd',
        )
