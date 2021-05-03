from django.core.management.base import BaseCommand
from articles.models import Article, Genre, Author
from datetime import datetime, timedelta
from random import randrange
from .functions import random_date
from .data_genre import data_genre
from .data_author import data_author
from .data_author import data_phone
import lorem


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        for name in data_genre:
            genre = Genre.objects.create(
                name=name,
            )

        for idx, name in enumerate(data_author):
            author = Author.objects.create(
                name=name,
                phone=data_phone[idx],
            )

        for i in range(1000):
            author_id = list(Author.objects.all().only('id'))
            genre_id = list(Genre.objects.all().only('id'))

            article = Article.objects.create(
                author=author_id[randrange(0, len(author_id))],
                genre=genre_id[randrange(0, len(genre_id))],
                title=lorem.sentence(),
                text=lorem.text(),
                published_at=random_date(),
            )

            
