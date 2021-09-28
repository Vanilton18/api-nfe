from rest_framework import serializers

from core_nfe import models


class NfeCustomSerializer(serializers.HyperlinkedModelSerializer):
    def get_field_names(self, declared_fields, info):
        fields = super().get_field_names(declared_fields, info)
        fields.insert(0, 'id')
        return fields


class CountrySerializer(NfeCustomSerializer):
    class Meta:
        model = models.Country
        fields = '__all__'
