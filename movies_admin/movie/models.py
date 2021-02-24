import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class Category(TimeStampedModel):
    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_('Категория'), max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')


class Genre(TimeStampedModel):
    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_('Жанр'), max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Жанр')
        verbose_name_plural = _('Жанры')


class Person(TimeStampedModel):
    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.TextField(_('Имя актера'))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Персона')
        verbose_name_plural = _('Персоны')


class RoleType(models.TextChoices):
    ACTOR = 'actor', _('Актер')
    WRITER = 'writer', _('Сценарист')
    DIRECTOR = 'director', _('Режиссер')


class PersonMovie(TimeStampedModel):
    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4, editable=False)
    movie = models.ForeignKey('Movie', verbose_name=_('Фильм'), on_delete=models.CASCADE)
    person = models.ForeignKey('Person', verbose_name=_('Персона'), on_delete=models.CASCADE)
    role = models.TextField(_('роль'), choices=RoleType.choices)

    def __str__(self):
        return f"{self.person} in {self.movie}"

    class Meta:
        verbose_name = _('Персона в фильме')
        verbose_name_plural = _('Персоны в фильме')


class Movie(TimeStampedModel):
    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_('Название фильма'), max_length=200)
    description = models.TextField(_('Описание'))
    create_date = models.DateField(_('Дата создания'))
    age_qualification = models.PositiveIntegerField(_('Возрастной ценз'), default=0)
    rating = models.FloatField(_('Рейтинг'), default=0)
    persons = models.ManyToManyField('Person', verbose_name=_('Люди'), through='PersonMovie')
    category = models.ForeignKey('Category', verbose_name=_('Категория'), related_name='movie_category',
                                 on_delete=models.SET_NULL, blank=True, null=True)
    genres = models.ManyToManyField(Genre, verbose_name=_('Жанры'), related_name='movie_genre')
    file = models.FileField(_('Путь до файла'), upload_to='media/files', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Фильм')
        verbose_name_plural = _('Фильмы')
