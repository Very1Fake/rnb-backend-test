from rnb_backend_test.settings import (
    INFURA_PROJECT_ID,
    CONTRACT_ABI,
    CONTRACT_ADDRESS,
)

from web3 import Web3
from web3.middleware.geth_poa import geth_poa_middleware


# Connection to target smart contract via Infura
def sc_handle():
    # Connect to Infura API provider
    w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/" + INFURA_PROJECT_ID))

    # Inject PoA middleware
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    # Check connection to provider
    if not w3.isConnected:
        raise Exception("Cannot connect to eth network")

    # Open contract handle and load ABI
    contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

    return contract, w3
