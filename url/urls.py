from django.urls import path, re_path

from . import views

app_name = 'url'
urlpatterns = [
    path('', views.index, name='index'),
    path('urls/', views.ListView.as_view(), name='urls'),
    re_path(r'^(?P<short>[A-Za-z0-9]{4})$', views.redirect_short, name='redirect'),
    re_path(r'^info/(?P<slug>[A-Za-z0-9]{4})$', views.DetailView.as_view(), name='info'),
]
