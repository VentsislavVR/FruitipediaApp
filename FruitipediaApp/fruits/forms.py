from django import forms

from FruitipediaApp.fruits.models import Category, Fruit


class CategoryModelForm(forms.ModelForm):
    # name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={'class': ''}
    #     )
    #
    # )
    class Meta:

        model = Category
        fields = '__all__'





class FruitModelForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
