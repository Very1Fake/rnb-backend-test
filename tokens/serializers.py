from rest_framework.serializers import ModelSerializer

from .models import Token


class TokenModelSerializer(ModelSerializer):
    class Meta:
        model = Token
        fields = "__all__"
