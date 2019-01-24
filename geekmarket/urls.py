"""geekmarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
import mainapp.views as controller

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', controller.index, name='home'),
    path('products/', controller.products, name='catalog'),
    path('products/<str:current_product_category>/', controller.products, name='catalog'),
    path('details/', controller.details, name='product'),
    path('details/<str:color>/', controller.details, name='product'),
    path('history/', controller.history, name='history'),
    path('showroom/', controller.showroom, name='showroom'),
    path('contacts/', controller.contacts, name='contacts')
]
