
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shop.urls')),
    path('product/', include('Product.urls')),
    path('order/', include('Orderapp.urls')),
    path('user/', include('Userapp.urls')),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root':  settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
