from rest_framework import serializers

from .models import Part, PartCategory, PartParameter, PartParameterTemplate


class PartParameterSerializer(serializers.ModelSerializer):
    """ Serializer for a PartParameter
    """

    class Meta:
        model = PartParameter
        fields = ('pk',
                  'part',
                  'template',
                  'name',
                  'value',
                  'units')


class PartSerializer(serializers.ModelSerializer):
    """ Serializer for complete detail information of a part.
    Used when displaying all details of a single component.
    """

    class Meta:
        model = Part
        fields = ('pk',
                  'name',
                  'IPN',
                  'description',
                  'category',
                  'stock')


class PartCategoryBriefSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartCategory
        fields = ('pk',
                  'name',
                  'description')


class PartCategoryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartCategory
        fields = ('pk',
                  'name',
                  'description',
                  'parent',
                  'path')


class PartTemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartParameterTemplate
        fields = ('pk',
                  'name',
                  'units',
                  'format')
