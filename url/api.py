from rest_framework import viewsets

from .models import Url, UrlLog
from .serializers import UrlSerializer, UrlLogSerializer


class UrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer


class UrlLogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows UrlLog to be viewed
    """
    queryset = UrlLog.objects.all()
    serializer_class = UrlLogSerializer

    def get_queryset(self):
        queryset = UrlLog.objects.all()
        url = self.request.query_params.get('url', None)
        if url is not None:
            queryset = queryset.filter(url=url).order_by('-time')
        return queryset
  

