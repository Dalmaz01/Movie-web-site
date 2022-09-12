from django.shortcuts import render
from . import models


def home(request):
    movies = models.Movie.objects.all()
    return render(request, 'base/index.html', {'movies': movies})


def movieDetail(request, pk):
    movie = models.Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'base/movie_detail.html', context)