from string import ascii_letters, digits
from random import choice

from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rnb_backend_test.settings import PRIVATE_KEY, GAS_TOKEN_CREATE, SERVER_ETH_ADDRESS

from .models import Token
from .utils import sc_handle
from .serializers import TokenModelSerializer


# TODO: Use form serializer for `create`, `list` views

# `create` view
# Creates a new token, registers it in the smart contract and writes it to the database
# Returns the metadata of the created token
@api_view(["POST"])
def tokens_create(request):
    data = request.data

    # Generate random string (0-9-a-zA-Z)
    unique_hash = "".join(choice(ascii_letters + digits) for _ in range(20))
    media_url = data["media_url"]
    owner = data["owner"]

    # Token record without transaction hash
    token = Token(unique_hash=unique_hash, media_url=media_url, owner=owner)

    contract, w3 = sc_handle()

    # Parse private key from settings
    account = w3.eth.account.from_key(PRIVATE_KEY)

    # Composed transaction
    tx = contract.functions.mint(owner, unique_hash, media_url).buildTransaction(
        {
            "chainId": 4,  # Rinkeby testnet
            "gas": GAS_TOKEN_CREATE,
            "maxFeePerGas": w3.toWei("2", "gwei"),
            "maxPriorityFeePerGas": w3.toWei("1", "gwei"),
            "from": SERVER_ETH_ADDRESS,
            "nonce": w3.eth.get_transaction_count(SERVER_ETH_ADDRESS),
        }
    )
    # Signed transaction
    signed_tx = w3.eth.account.sign_transaction(tx, account.key)
    # Hash of sent transaction
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    # Write token to database after transaction finished
    token.tx_hash = tx_hash.hex()
    token.save()

    return Response(TokenModelSerializer(token).data)


# `list` view
# Returns a list of metadata of created tokens via this server
# Supports pagination:
# - `page`: page number
# - `size`: page size
@api_view(["GET"])
def tokens_list(request):
    params = request.query_params

    page = int(params.get("page", 1))
    size = int(params.get("size", 20))  # TODO: Page size limits

    query = Paginator(Token.objects.order_by("-id"), size).page(page)
    serializer = TokenModelSerializer(query, many=True)
    return Response({"page": page, "size": size, "tokens": serializer.data})


# `total_supply`
# Returns the total number of tokens registered in the smart contract
@api_view(["GET"])
def tokens_total_supply(_):
    # Open contract handle
    contract, _ = sc_handle()

    # Call contract `totalSupply()` method
    total_supply = contract.functions.totalSupply().call()

    return Response({"total_supply": total_supply})
