from django.urls import path
from .views import (
    home,create_maingroup,list_maingroup,create_partgroup,create_product,create_productgroup,update_maingroup,update_partgroup,
    update_product,update_productgroup,load_maingroup,delete_maingroup,delete_partgroup
    )

app_name = 'products'
urlpatterns = [
    path('',create_maingroup,name='maingroup'),
    path('main-group/<int:id>/update',update_maingroup,name='update_maingroup'),
    path('main-group/<int:id>/delete',delete_maingroup,name='delete_maingroup'),

    path('list-main-group',list_maingroup,name='list-maingroup'),

    path('part-group',create_partgroup,name='partgroup'),
    path('part-group/<int:id>/update',update_partgroup,name='update_partgroup'),
    path('part-group/<int:id>/delete',delete_partgroup,name='delete_partgroup'),

    path('product-group',create_productgroup,name='productgroup'),
    path('product-group/<int:id>/update',update_productgroup,name='update_productgroup'),

    path('product',create_product,name='product'),
    path('product/<int:id>/update',update_product,name='update_product'),


    path('ajax/dropdown-list',load_maingroup,name='ajax-dropdown'),

]

