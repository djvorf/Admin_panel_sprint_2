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
