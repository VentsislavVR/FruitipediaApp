from django.core.exceptions import ValidationError


def only_alphabet(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Name must contain only letters!')

