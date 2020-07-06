from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from geoip import geolite2
#from django.contrib.gis.geoip2 import GeoIP2

from .models import Url, UrlForm, UrlLog


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    if request.method == 'POST':
        form =  UrlForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect(reverse('url:info', args=(instance.short,)))
    else:
        form = UrlForm()
    return render(request, 'url/index.html', {'form': form})


def redirect_short(request, short):
    url = get_object_or_404(Url, short=short)
    url.times_visited += 1
    url.save()
    ip = get_client_ip(request)
    location = geolite2.lookup(ip)
    l = UrlLog(url=url, source=ip)
    if location:
        l.country_code = location.country
    l.save()
    return redirect(url.url)


class DetailView(generic.DetailView):
    model = Url
    slug_field = 'short'

class ListView(generic.ListView):
    model = Url
