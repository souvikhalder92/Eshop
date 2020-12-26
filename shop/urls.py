
from django.urls import path
from .views import home,product_single,category_product,about,contact,SearchView

urlpatterns = [
    path('',home,name='home'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact_dat'),
     path('product/<int:id>/',product_single,name='product_single'),
    path('category/<int:id>/<slug:slug>',category_product,name='category_product'),
    path('search/',SearchView,name='SearchView')
]