# R'n'B Backend Test

A simple Django backend service that interacts with an ERC-721 standard contract on the
Ethereum blockchain (Rinkeby testnet) and allows users to interact with it via a REST API.

## Tech Stack

Language: `Python 3.10.5`

Web framework: `Django 3.2.13`

Blockchain library: `Web3.py 5.29.2`

## Usage

### Prerequisites

Install `poetry` to manage virtualenv and dependencies:

```bash
pip install poetry
```

### Launch

#### Local

First setup virtualenv:

```bash
poetry install
```

Then apply migration (if you haven't done this yet):

```bash
poetry run python manage.py migrate 
```

And now you can run the server:

```bash
poetry run python manage.py runserver
```

#### Docker

To launch docker just enter:

```bash
make up_build
```

To make migrations:

```bash
make migrate
```

## Features

- [x] Docker Image
  - [x] Image Building
  - [x] Compose
- [x] SQLite Database (Models)
- [ ] Swagger (drf-yasg)
- [x] Views
  - [x] /tokens/create
  - [x] /tokens/list
    - [x] Pagination
  - [x] /tokens/total_supply
- [x] Configuration (.env)
- [x] Integration with web3

## .ENV file configuration

- DJANGO_PORT - Port that django will use (docker only)
- DOCKER_EXPOSE_PORT - External port (docker only)
- INFURA_PROJECT_ID - Infura project id. Used by Web3.py to make RPC calls
- SERVER_ETH_ADDRESS - Ethereum address that will be used by server to sign transactions
- PRIVATE_KEY - Private key for server
- CONTRACT_ADDRESS - Ethereum address of target smart contract
- GAS_TOKEN_CREATE - The amount of gas for token minting (default: `400000`)
