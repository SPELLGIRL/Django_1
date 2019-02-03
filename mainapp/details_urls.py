from django.urls import path

import mainapp.views as controller

app_name = 'mainapp'

urlpatterns = [
    path('<int:product_id>/', controller.details, name='product'),
    path('<int:product_id>/<str:color>/', controller.details,
         name='color'),

]
