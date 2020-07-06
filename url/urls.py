from django.urls import path, re_path, include
from rest_framework import routers

from . import views
from . import api

app_name = 'url'

router = routers.DefaultRouter()
router.register(r'log', api.UrlLogViewSet)
router.register(r'url', api.UrlViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('urls/', views.ListView.as_view(), name='urls'),
    re_path(r'^(?P<short>[A-Za-z0-9]{4})$', views.redirect_short, name='redirect'),
    re_path(r'^info/(?P<slug>[A-Za-z0-9]{4})$', views.DetailView.as_view(), name='info'),
]
