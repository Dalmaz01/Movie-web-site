from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name='home'),
    path('movie_detail/<int:pk>', views.movieDetail, name='movie_detail'),
]