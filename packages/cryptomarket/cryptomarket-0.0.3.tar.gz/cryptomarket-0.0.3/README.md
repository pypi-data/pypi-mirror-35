# CryptoMarket
The official Python library for the [CryptoMarket API v1](https://developers.cryptomkt.com).

# Installation
To install Cryptomarket, simply use pip:
```
pip install cryptomarket
```
# Documentation

The first things you'll need to do is [sign up with CryptoMarket](https://www.cryptomkt.com/account/register).

## API Key + Secret
If you're writing code for your own CryptoMarket account, [enable an API key](https://www.cryptomkt.com/account2#api_tab).

Next, create a Client object for interacting with the API:

```
from cryptomarket.exchange.client import Client

client = Client(api_key, api_secret)
```

# Usage

## [Market Data](https://developers.cryptomkt.com/es/#mercado)

### Get markets
```
client.get_markets()
```
