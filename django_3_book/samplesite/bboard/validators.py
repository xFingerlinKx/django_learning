from django.core.exceptions import ValidationError


def validate_even(val):
    """
    Валидатор для поля типа FloatField.
    Число должно быть не отрицательым.
    """
    if val < 0:
        raise ValidationError(
            message=f'Число {val} меньше нуля',
            code='negative',
        )
