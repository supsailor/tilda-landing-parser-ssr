from landing.models.tilda_page import TildaPageModel
from rest_framework import generics
from landing.serializers.tilda_page import TildaPageSingleSerializer, TildaPageListSerializer


class TildaPageListApi(generics.ListAPIView):
    queryset = TildaPageModel.objects.all()
    serializer_class = TildaPageListSerializer


class TildaPageSingleApi(generics.RetrieveAPIView):
    queryset = TildaPageModel.objects.all()
    serializer_class = TildaPageSingleSerializer
