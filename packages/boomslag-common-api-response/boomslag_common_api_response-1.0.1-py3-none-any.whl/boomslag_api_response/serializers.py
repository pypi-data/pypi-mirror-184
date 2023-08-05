from rest_framework import serializers

class APIResponseSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    data = serializers.DictField(required=False)
    error = serializers.CharField(required=False)