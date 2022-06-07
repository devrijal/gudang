from django.urls import path

from . import views

urlpatterns = [
    path('stok', views.stok, name='stok'),
]