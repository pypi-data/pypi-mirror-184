from rest_framework import serializers

class AnyField(serializers.Field):
    def to_representation(self, value):
        return value
    
    def to_internal_value(self, data):
        return data

class APIResponseSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    status = serializers.CharField(required=False)
    count = serializers.IntegerField(required=False)
    next = serializers.URLField(required=False)
    previous = serializers.URLField(required=False)
    data = AnyField(required=False)
    error = serializers.CharField(required=False)
