from django.urls import path, include
from .views import home
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('add_stocks.html', views.add_stocks, name='add_stocks'),
    path('delete/<stock_id>', views.delete, name='delete'),
    path('delete_stocks.html', views.delete_stocks, name='delete_stocks'),
]
