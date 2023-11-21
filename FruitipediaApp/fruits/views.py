from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from FruitipediaApp.fruits.forms import CategoryModelForm, FruitModelForm
from FruitipediaApp.fruits.models import Fruit


# Create your views here.
def index(request):
    return render(request, 'templates/common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()
    context = {
        'fruits': fruits
    }

    return render(
        request,
        'templates/common/dashboard.html',
        context)





def details_fruit(request, fruit_pk):
    # fruit = Fruit.objects.filter(pk=fruit_pk).last()
    fruit = get_object_or_404(Fruit, pk=fruit_pk)
    context = \
        {'fruit': fruit}
    return render(
        request,
        'templates/fruits/details-fruit.html',
        context)


def edit_fruit(request, fruit_pk):
    fruit = Fruit.objects.filter(pk=fruit_pk).get()

    if request.method == 'GET':
        form = FruitModelForm(instance=fruit)
    else:
        form = FruitModelForm(request.POST,instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
            'form': form,
            'fruit': fruit,
        }
    return render(
        request,
        'templates/fruits/edit-fruit.html',
        context
    )


def delete_fruit(request, fruit_pk): #TODO
    return render(request, 'templates/fruits/delete-fruit.html')


# def category_create(request):
#     if request.method == 'POST':
#
#         form = CategoryModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('create-category')
#     else:
#         form = CategoryModelForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(
#         request,
#         'templates/categories/create-category.html',
#         context
#     )
class CategoryFormView(FormView):
    form_class = CategoryModelForm
    template_name = 'templates/categories/create-category.html'
    success_url = reverse_lazy('create-category')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class FruitFormView(FormView):
    form_class = FruitModelForm
    template_name = 'templates/fruits/create-fruit.html'
    success_url = reverse_lazy('templates/fruits/create-fruit.html')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
