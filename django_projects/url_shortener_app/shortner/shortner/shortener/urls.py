from django.contrib import admin
from django.urls import path
from . import views

app_name = 'shortener'
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('<str:shortURL>/', views.index, name='index_with_short'),
    path('short', views.short, name='short'),
    path('<str:shortURL>/', views.redirect, name='redirect'),    
]