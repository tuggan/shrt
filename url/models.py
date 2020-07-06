from django.db import models
from django.forms import ModelForm
from django import forms

from .lib import generator

class Url(models.Model):
    short = models.CharField(max_length=4, unique=True, null=False, blank=False, default=generator.random_string)
    url = models.URLField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    last_visited = models.DateTimeField(auto_now=True, null=False, blank=False)
    times_visited = models.BigIntegerField(default=0, blank=False)
    public = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self):
        return f'{self.short} - {self.url}'
    

class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ['url', 'public']
        widgets = {
            'url': forms.TextInput(attrs={'placeholder': 'URL'}),
        }


class UrlLog(models.Model):
    url = models.ForeignKey(Url, on_delete=models.CASCADE, null=False, blank=False)
    time = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    source = models.GenericIPAddressField(null=False, blank=False)
    country_code = models.CharField(max_length=2, null=True)

    def __str__(self):
        return f'{self.url.short} - {self.source} ({self.country_code}): {self.time}'

