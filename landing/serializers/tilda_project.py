from landing.models.tilda_project import TildaProjectModel
from rest_framework import serializers


class TildaProjectSingleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TildaProjectModel
        fields = [
            'id',
            'external_id',
            'title',
            'description',
            'date_created',
            'date_updated',
        ]


class TildaProjectListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TildaProjectModel
        fields = [
            'id',
            'external_id',
            'title',
            'description',
            'date_created',
            'date_updated',
        ]
