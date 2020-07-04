from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic

from .models import Url, UrlForm

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
    return redirect(url.url)

class DetailView(generic.DetailView):
    model = Url
    slug_field = 'short'

class ListView(generic.ListView):
    model = Url
