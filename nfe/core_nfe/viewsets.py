from rest_framework import viewsets

from core_nfe import models, serializers


class CountryViewSet(viewsets.ModelViewSet):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer
