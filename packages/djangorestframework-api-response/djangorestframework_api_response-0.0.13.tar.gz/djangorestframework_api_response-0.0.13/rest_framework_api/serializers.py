from rest_framework import serializers

class APIResponseSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    status = serializers.CharField(required=False)
    count = serializers.IntegerField(required=False)
    next = serializers.URLField(required=False)
    previous = serializers.URLField(required=False)
    data = serializers.Field(required=False)
    error = serializers.CharField(required=False)

    def to_representation(self, obj):
        # Make sure the data field is included in the serialized representation
        self.fields['data'] = serializers.Field()
        return super().to_representation(obj)
