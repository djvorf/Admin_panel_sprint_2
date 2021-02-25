from django.urls import path

from .views import MovieDetailView, MovieView

urlpatterns = [
    path('movies/', MovieView.as_view()),
    path('movie/<uuid:uuid>', MovieDetailView.as_view()),
]
