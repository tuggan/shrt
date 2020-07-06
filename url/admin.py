from django.contrib import admin

from .models import Url, UrlLog

admin.site.register(Url)
admin.site.register(UrlLog)
