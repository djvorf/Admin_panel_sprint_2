from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView

from movie.models import Movie, PersonMovie, RoleType


class MovieMixin:
    model = Movie
    http_method_names = ['get']

    def get_queryset(self):
        self.queryset = Movie.objects.prefetch_related('genres', 'persons').values(
            'id', 'title', 'description', 'create_date', 'age_qualification', 'rating', 'file'
        ).annotate(
            type=ArrayAgg('category__title', distinct=True),
            genres=ArrayAgg('genres__title', distinct=True),
            actors=ArrayAgg('persons__full_name', distinct=True, filter=Q(personmovie__role=RoleType.ACTOR)),
            writers=ArrayAgg('persons__full_name', distinct=True, filter=Q(personmovie__role=RoleType.WRITER)),
            directors=ArrayAgg('persons__full_name', distinct=True, filter=Q(personmovie__role=RoleType.DIRECTOR))
        )
        return self.queryset.all()

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class MovieView(MovieMixin, BaseListView):
    paginate_by = 2

    def get_context_data(self, **kwargs):
        page_size = self.get_paginate_by(queryset=self.queryset)
        paginator, page, queryset, is_paginator = self.paginate_queryset(self.queryset, page_size=page_size)
        context = {
            "count": paginator.count,
            "total_pages": paginator.num_pages,
            "prev": page.previous_page_number() if page.has_previous() else page.number,
            "next": page.next_page_number() if page.has_next() else page.number,
            "result": list(queryset)
        }
        return context


class MovieDetailView(MovieMixin, BaseDetailView):
    slug_field = 'id'
    pk_url_kwarg = 'uuid'

    def get_context_data(self, **kwargs):
        # Можно ли использовать просто return self.get_object()? Вроде так же возвращает нужный фильм

        return super().get_context_data(**kwargs)['object']
