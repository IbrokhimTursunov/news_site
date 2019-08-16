from rest_framework import viewsets
from api.serializers import NewsSerializer

from api.models import News


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer



