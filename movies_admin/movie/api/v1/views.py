from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView

from movie.models import Movie


def get_all_movies():
    movies = Movie.objects.prefetch_related('genres', 'actors', 'writers', 'directors', 'genres')
    movies_list = []
    for movie in movies:
        movies_list.append({
            "id": movie.id,
            "title": movie.title,
            "description": movie.description,
            "creation_date": movie.create_date,
            "rating": movie.rating,
            "type": movie.category.title,
            "actors": [f"{actor.get('first_name')} {actor.get('last_name')}" for actor in
                       movie.actors.values('first_name', 'last_name')],
            "writers": [f"{actor.get('first_name')} {actor.get('last_name')}" for actor in
                        movie.writers.values('first_name', 'last_name')],
            "directors": [f"{actor.get('first_name')} {actor.get('last_name')}" for actor in
                          movie.directors.values('first_name', 'last_name')],
            "genres": [genre.get('title') for genre in movie.genres.values('title')],
        })
    return movies_list


class MovieMixin:
    model = Movie
    http_method_names = ['get']
    movies = get_all_movies()

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class MovieView(MovieMixin, BaseListView):
    paginate_by = 1

    def get_context_data(self, **kwargs):
        page_size = self.get_paginate_by(queryset=self.movies)
        result = self.paginate_queryset(queryset=self.movies, page_size=page_size)
        context = {
            "count": len(result),
            "total_pages": int(result[0].num_pages),
            "prev": int(result[1].previous_page_number() if result[1].has_previous() else result[1].number),
            "next": int(result[1].next_page_number() if result[1].has_next() else result[1].number),
            "result": result[2][0]
        }
        return context


class MovieDetailView(MovieMixin, BaseDetailView):

    def get_context_data(self, **kwargs):
        for movie in self.movies:
            if str(movie.get('id')) == self.kwargs.get('pk'):
                context = movie
                return context
