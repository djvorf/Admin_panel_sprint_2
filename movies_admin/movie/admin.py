from django.contrib import admin
from .models import Movie, Category, Genre, Person, PersonMovie
from django.utils.translation import gettext_lazy as _


@admin.register(PersonMovie)
class PersonMovieAdmin(admin.ModelAdmin):
    list_display = ('person', 'movie')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)


class GenreInLine(admin.TabularInline):
    model = Movie.genres.through
    extra = 0
    verbose_name = _('Жанр')
    verbose_name_plural = _('Жанры')


class PersonMovieInLine(admin.TabularInline):
    model = PersonMovie
    extra = 0
    verbose_name = _('Персона')
    verbose_name_plural = _('Персоны')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'create_date')
    fields = ('title', 'description', 'create_date', 'age_qualification', 'rating', 'file', 'category')
    list_filter = ('category', 'age_qualification', 'create_date', 'title')
    search_fields = ('title', 'description', 'id', 'category', 'age_qualification', 'create_date')
    inlines = [GenreInLine, PersonMovieInLine]
