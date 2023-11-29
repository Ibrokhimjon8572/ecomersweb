from django.urls import path
from .views import main, products


urlpatterns = [
    path('product/', main, name='main'),
    path('', products, name='products')
]