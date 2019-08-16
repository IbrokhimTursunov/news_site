from django.db import models


class News(models.Model):
    title = models.CharField(default='', blank=True, primary_key=False, max_length=2048)
    content = models.TextField(default='', blank=True, primary_key=False)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
