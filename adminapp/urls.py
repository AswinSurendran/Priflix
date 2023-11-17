from django.urls import path
from.import views

urlpatterns = [
    path('',views.base,name='base'),
    path(' categories',views.categories,name='categories'),
    path('catalog',views.catalog,name='catalog'),
    path('additem',views.additem,name='additem'),
    path('Catalogs',views.Catalogs,name='Catalogs'),
    path('contacttable',views.contacttable,name='contacttable'),
    path('registable',views.registable,name='registable'),
    path('pricetable',views.pricetable,name='pricetable'),
    path('price',views.price,name='price'),
    path('pricedata',views.pricedata,name='pricedata')
    
]
