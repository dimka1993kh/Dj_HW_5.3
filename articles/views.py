from django.views.generic import ListView
from django.shortcuts import render

from .models import Article


def articles_list(request):
    template_name = 'articles/news.html'

    news = Article.objects.all().select_related('author', 'genre').defer('author__phone')
    # news = Article.objects.all()

    context = {
        'object_list': news,
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template_name, context)
