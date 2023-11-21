from django.urls import path, include

from FruitipediaApp.fruits.views import index, dashboard, details_fruit, edit_fruit, \
    delete_fruit, CategoryFormView, FruitFormView

urlpatterns = (
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create-fruit/', FruitFormView.as_view(), name='create-fruit'),
    path('<int:fruit_pk>/', include([
        path('details/', details_fruit, name='details-fruit'),
        path('edit/', edit_fruit, name='edit-fruit'),
        path('delete/', delete_fruit, name='delete-fruit'),
    ])),
         path('create-category/',CategoryFormView.as_view(), name='create-category'),
         )
