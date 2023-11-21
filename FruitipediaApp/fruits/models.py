from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from FruitipediaApp.fruits.validators import only_alphabet


class Category(models.Model):
    name = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.name

class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            only_alphabet,
        ]
    )
    image_url = models.URLField()

    description = models.TextField(
        null=False,
        blank=False)
    nutrition = models.TextField(
        null=True,
        blank=True,
    )