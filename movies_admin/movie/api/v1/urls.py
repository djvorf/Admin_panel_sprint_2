from django.urls import path

from .views import MovieDetailView, MovieView

urlpatterns = [
    path('movies/', MovieView.as_view()),
   # path('movie/<str:pk>', MovieDetailView.as_view()),
]
