# projeto/urls.py

from django.contrib import admin
from django.urls import path, include
from meuapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('meuapp/', include('meuapp.urls')),
    #path('admin/', admin.site.urls),
]
