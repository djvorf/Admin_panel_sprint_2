from django.contrib import admin
from .models import Movie, Category, Genre, Person
from django.utils.translation import gettext_lazy as _


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


class ActorInLine(admin.TabularInline):
    model = Movie.actors.through
    extra = 0
    verbose_name = _('Актер')
    verbose_name_plural = _('Актеры')


class WriterInLine(admin.TabularInline):
    model = Movie.writers.through
    extra = 0
    verbose_name = _('Сценарист')
    verbose_name_plural = _('Сценаристы')


class DirectorInLine(admin.TabularInline):
    model = Movie.directors.through
    extra = 0
    verbose_name = _('Режиссер')
    verbose_name_plural = _('Режиссеры')


class GenreInLine(admin.TabularInline):
    model = Movie.genres.through
    extra = 0
    verbose_name = _('Жанр')
    verbose_name_plural = _('Жанры')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'create_date')
    fields = ('title', 'description', 'create_date', 'age_qualification', 'file', 'category')
    list_filter = ('category', 'age_qualification', 'create_date', 'title')
    search_fields = ('title', 'description', 'id', 'category', 'age_qualification', 'create_date')
    inlines = [ActorInLine, WriterInLine, DirectorInLine, GenreInLine]
