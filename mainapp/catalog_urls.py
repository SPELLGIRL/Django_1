from django.urls import path

import mainapp.views as controller

app_name = 'mainapp'

urlpatterns = [
    path('<str:current_product_category>/',
         controller.products, name='catalog'),
    # path('', controller.products, name='catalog')
]
