from django.db import models
from django.db.models import Q
from django import forms

class SearchQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query=='':
            return None
        lookups = Q(title__icontains=query) | Q(body__contains=query)
        return self.filter(lookups)



class PostManager(models.Manager):
    def get_queryset(self):
        return SearchQuerySet(self.model, using=self.db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)




class TagField(forms.Field):
    def to_python(self, value):
        if not value:
            return []
        return value.split(',')
