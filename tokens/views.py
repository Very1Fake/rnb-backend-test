from rest_framework.decorators import api_view
from rest_framework.response import Response


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
def tokens_list(request):
    return Response({"message": "/tokens/list endpoint"})


@api_view(["GET"])
def tokens_total_supply(request):
    return Response({"message": "/tokens/total_supply endpoint"})
