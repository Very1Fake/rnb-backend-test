from rest_framework.serializers import ModelSerializer

from .models import Token


# Serializer for `Token` model
class TokenModelSerializer(ModelSerializer):
    class Meta:
        model = Token
        fields = "__all__"
