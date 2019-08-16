from django.db import models


class News(models.Model):
    title = models.CharField(default='', blank=True, primary_key=False)
    content = models.TextField(default='', blank=True, primary_key=False)
