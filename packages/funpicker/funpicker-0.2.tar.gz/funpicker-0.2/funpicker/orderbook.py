import ccxt
from funpicker.util.converter import convert_usd
def get_exchange(exchange_id):
    exchange_class = getattr(ccxt, exchange_id)
    exchange = exchange_class({
        'timeout': 30000,
        'enableRateLimit': True,
    })
    exchange.load_markets()
    return exchange

def get_exchange_with_keys(exchange_id, API_KEY, API_SECRET):
    exchange_class = getattr(ccxt, exchange_id)
    exchange = exchange_class({
        'timeout': 30000,
        'enableRateLimit': True,
        'apiKey': API_KEY,
        'secret': API_SECRET,
    })
    exchange.load_markets()
    return exchange


def get_balance(key, secret, _exchange="binance"):
    exc = get_exchange_with_keys(_exchange, key, secret)
    try:
        balance = exc.fetch_balance()
        return balance
    except Exception as e:
        return {}

def get_orderbook(crypto, fiat, exchange="binance"):
    exc = get_exchange(exchange)
    if fiat == "USD":
        fiat = convert_usd(exchange)
    symbol = "{}/{}".format(crypto, fiat)
    try:
        order_book = exc.fetch_order_book(symbol)
        return order_book
    except Exception as e:
        print(str(e))
        return []
    



if __name__ == "__main__":
    print(get_orderbook("KMD", "BTC", exchange='binance'))