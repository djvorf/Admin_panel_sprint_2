from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class Category(TimeStampedModel):
    title = models.CharField(_('Категория'), max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')


class Genre(TimeStampedModel):
    title = models.CharField(_('Жанр'), max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Жанр')
        verbose_name_plural = _('Жанры')


class Person(TimeStampedModel):
    first_name = models.CharField(_('Имя'), max_length=150)
    last_name = models.CharField(_('Фамилия'), max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _('Персона')
        verbose_name_plural = _('Персоны')


class Movie(TimeStampedModel):
    title = models.CharField(_('Название фильма'), max_length=200)
    description = models.TextField(_('Описание'))
    create_date = models.DateField(_('Дата создания'))
    age_qualification = models.PositiveIntegerField(_('Возврастной ценз'), default=0)
    category = models.ForeignKey(Category, verbose_name=_('Категрия'), related_name='movie_category',
                                 on_delete=models.SET_NULL, blank=True, null=True)
    rating = models.FloatField(_("Рейтинг"), default=0)
    actors = models.ManyToManyField(Person, verbose_name=_('Актеры'), related_name='movie_actor')
    writers = models.ManyToManyField(Person, verbose_name=_('Сценаристы'), related_name='movie_writer')
    directors = models.ManyToManyField(Person, verbose_name=_('Режиссеры'), related_name='movie_director')
    genres = models.ManyToManyField(Genre, verbose_name=_('Жанры'), related_name='movie_genre')
    file = models.FileField(_('Путь до файла'), upload_to='media/files', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Фильм')
        verbose_name_plural = _('Фильмы')
