from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import NewsSerializer

from api.models import News


class HomePage(TemplateView):
    template_name = 'index.html'


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-created')
    serializer_class = NewsSerializer


class SearchNews(APIView):

    @staticmethod
    def get(request):
        instance = request.GET.get('instance', '')
        words = instance.split()

        ids = set()
        for word in words:
            items = News.objects.filter(title__icontains=word)
            ids |= {item.id for item in items}

        queryset = News.objects.filter(pk__in=ids).order_by('-created')
        serializer = NewsSerializer(data=queryset, many=True)
        serializer.is_valid()
        return Response(serializer.data)
