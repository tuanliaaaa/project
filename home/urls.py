from django.urls import path
from . import views
urlpatterns = [
    path('index.html',views.index),
    path('watches.html',views.watches),
    path('card.html',views.card),
    path('singerProduct.html',views.singerProduct),
    path('search.html',views.search),
]