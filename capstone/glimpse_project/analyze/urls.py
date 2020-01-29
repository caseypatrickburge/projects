from django.urls import path
from . import views 

urlpatterns = [
    path('search/', Search.as_view(), name='search'),
]