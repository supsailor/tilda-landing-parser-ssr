from landing.models.tilda_page import TildaPageModel
from rest_framework import serializers


class TildaPageSingleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TildaPageModel
        fields = [
            'id',
            'external_id',
            'title',
            'description',
            'css',
            'js',
            'images',
            'date_created',
            'date_updated',
            'html'
        ]


class TildaPageListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TildaPageModel
        fields = [
            'id',
            'external_id',
            'title',
            'description',
            'date_created',
            'date_updated',
        ]
