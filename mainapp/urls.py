from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('mainapp/genres/', views.get_api_genres, name='genres'),
    path('mainapp/actors/', views.get_api_actors, name='actors'),
    path('mainapp/directors/', views.get_api_directors, name='directors'),

]
