import ccxt


def private_self():
    exchange = exchange_class({
        'apiKey': 'you_api_key',
        'secret': 'you_secret',
        'timeout': 30000,
        'enableRateLimit': True,
    })


def init():
    list = ccxt.exchanges
    print(list)

    binance_exchange = ccxt.binance(
        {'timeout': 15000, 'enableRateLimit': True})
    print(binance_exchange.id,
          binance_exchange.name,
          binance_exchange.urls,
          binance_exchange.iso8601(binance_exchange.milliseconds()))

    if(binance_exchange.has['fetchOHLCV']):
        binance_exchange.load_markets()
        print(binance_exchange.fetch_ohlcv('BTC/USDT', '1d'))


init()
