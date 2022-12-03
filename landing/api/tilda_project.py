from landing.models.tilda_project import TildaProjectModel
from rest_framework import generics
from landing.serializers.tilda_project import TildaProjectSingleSerializer, TildaProjectListSerializer


class TildaProjectListApi(generics.ListAPIView):
    queryset = TildaProjectModel.objects.all()
    serializer_class = TildaProjectListSerializer


class TildaProjectSingleApi(generics.RetrieveAPIView):
    queryset = TildaProjectModel.objects.all()
    serializer_class = TildaProjectSingleSerializer
