from rest_framework import serializers

class Field:
    def to_representation(self, data):
        # Convert the data into a serializable representation
        return data

class APIResponseSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    status = serializers.CharField(required=False)
    count = serializers.IntegerField(required=False)
    next = serializers.URLField(required=False)
    previous = serializers.URLField(required=False)
    data = Field(required=False)
    error = serializers.CharField(required=False)
