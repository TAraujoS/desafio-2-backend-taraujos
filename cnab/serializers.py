from rest_framework import serializers
from .models import Documentation


class FileSerializer(serializers.Serializer):
    file = serializers.FileField()


class DocumentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documentation
        fields = "__all__"

    def create(self, validated_data):
        transaction, _ = Documentation.objects.get_or_create(**validated_data)
        return transaction
