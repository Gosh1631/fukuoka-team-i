from django.urls import path

from . import views

appname="coin_cal"
urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.predict, name="predict"), 
]