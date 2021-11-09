from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_api_genres, name='home'),
    # path('', views.get_api_actors, name='home'),
    # path('', views.get_api_directors, name='home'),

]
