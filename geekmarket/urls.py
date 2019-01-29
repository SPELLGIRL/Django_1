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
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
import mainapp.views as controller

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('mainapp.catalog_urls', namespace='catalog')),
    path('products/', controller.products, name='catalog'),
    path('details/<str:color>/', controller.details, name='product'),
    path('details/', controller.details, name='product'),
    path('history/', controller.history, name='history'),
    path('showroom/', controller.showroom, name='showroom'),
    path('contacts/', controller.contacts, name='contacts'),
    path('<str:current_product_category>/', controller.index, name='home'),
    path('', controller.index, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
