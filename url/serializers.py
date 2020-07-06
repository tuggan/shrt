from rest_framework import serializers

from .models import Url, UrlLog


class UrlSerializer(serializers.ModelSerializer):
    #urlLog = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Url
        fields = ['short', 'url', 'created', 'last_visited', 'times_visited']
        read_only_fields = fields


class UrlLogSerializer(serializers.ModelSerializer):
    url = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UrlLog
        fields = ['url', 'time', 'country_code']
        read_only_fields = fields

