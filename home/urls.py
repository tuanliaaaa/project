from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('home',views.index,name='home'),
    path('watches',views.watches,name='watch'),
    path('watches/showAll',views.showAll,name='watch'),
    path('card',views.card,name='card'),
    path('singerProduct/<int:id>/',views.singerProduct,name='singerProduct'),
]