
from django.urls import path

from Product.views import Comment_Add

urlpatterns = [

     path('Comment_Add/<int:id>/',Comment_Add, name='comment_add'),
]
