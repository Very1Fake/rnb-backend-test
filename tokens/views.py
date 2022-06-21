from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Token
from .utils import sc_handle
from .serializers import TokenModelSerializer


@api_view(["POST"])
def tokens_create(request):
    data = request.data

    media_url = data["media_url"]
    owner = data["owner"]

    return Response(
        {
            "message": "/tokens/create endpoint",
            "data": {"media_url": media_url, "owner": owner},
        }
    )


# TODO: Add pagination
@api_view(["GET"])
def tokens_list(_):
    query = Token.objects.all()
    serializer = TokenModelSerializer(query, many=True)
    return Response({"tokens": serializer.data})


@api_view(["GET"])
def tokens_total_supply(_):
    # Open contract handle
    contract = sc_handle()

    # Call contract `totalSupply()` method
    total_supply = contract.functions.totalSupply().call()

    return Response({"total_supply": total_supply})
