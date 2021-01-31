from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path(r'user', csrf_exempt(views.index), name='index'),#untuk file user
    path('user/<int:id>', csrf_exempt(views.show), name='show'),
    path(r'foods', csrf_exempt(views.indexfood), name='indexfood'),#untuk file foods
    path('foods/<int:id>', csrf_exempt(views.showfood), name='showfood'),
    path(r'pesanans', csrf_exempt(views.pesanansindex), name='pesanansindex'),#untuk file pesanans
    path('pesanans/<int:id>', csrf_exempt(views.pesanansshow), name='showfood'),
]