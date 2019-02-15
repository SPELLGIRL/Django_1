from django.urls import path

from adminapp.views import users, categories, products

app_name = 'adminapp'

urlpatterns = [
    # users
    path('users/index/', users.index, name='users'),
    path('users/create/', users.create, name='user_create'),
    path('users/read/<int:id>', users.read, name='user_read'),
    path('users/update/<int:id>', users.update, name='user_update'),
    path('users/delete/<int:id>', users.delete, name='user_delete'),

    # categories
    path('categories/index/', categories.index, name='categories'),
    path('categories/create/', categories.create, name='category_create'),
    path('categories/read/<int:id>', categories.read, name='category_read'),
    path('categories/update/<int:id>', categories.update,
         name='category_update'),
    path('categories/delete/<int:id>', categories.delete,
         name='category_delete'),

    # products
    path('products/create/<int:pk>', products.create, name='product_create'),
    path('products/read/<int:id>', products.read, name='product_read'),
    path('products/list/<int:pk>', products.list_by_category,
         name='products'),
    path('products/update/<int:id>', products.update, name='product_update'),
    path('products/delete/<int:id>', products.delete, name='product_delete'),
]
