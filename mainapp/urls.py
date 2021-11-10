from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('api/genres/', views.get_api_genres, name='genres'),
    path('api/actors/', views.get_api_actors, name='actors'),
    path('api/directors/', views.get_api_directors, name='directors'),

]
