from django.urls import path
from . import views 

urlpatterns = [
    path('', views.analyze, name='analyze'),
    path('sentiment/', views.sentiment_return, name='sentiment')
]