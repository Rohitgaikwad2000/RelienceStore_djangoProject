"""
URL configuration for RelianceStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Relience.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload_csv/', upload_csv, name = "upload_csv"),
    path('all_products/', all_products, name = "all_products"),
    path('add_product/', add_product, name = "add_product"),
    path('update_product/<int:id>', update_product, name = "update_product"),
    path('delete_product/<int:id>', delete_product, name = "delete_product"),
    path('deleted_product/', deleted_product, name = "deleted_product"),
    path('restore_product/<int:id>', restore_product, name = "restore_product"),
    path('permanantly_delete/<int:id>', permanantly_delete, name = "permanantly_delete"),




]

