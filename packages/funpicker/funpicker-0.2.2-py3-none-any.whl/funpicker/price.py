import ccxt
import time
# import cryptocompare
import requests







def get_price(crypto, curr="USD", exchange='CCCAGG'):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}&e={}'.format(
            crypto, curr, exchange)
    
    resp = requests.get(url=url)
    # print(resp.json())
    # data = json.loads(resp.text)
    try:
        return {**resp.json(), **{"crypto": "BTC", "exchange": exchange, "timestamp": time.time(), "type": "price", "period": "minute"}}
    except Exception:
        return []

def get_historical_price(crypto, curr="USD", exchange='CCCAGG', period="minute", limit=1400):
    url = 'https://min-api.cryptocompare.com/data/{0}?fsym={1}&tsym={2}&limit={3}&aggregate=1&e={4}'.format(
            "histo" + period, crypto, curr, limit, exchange)
    resp = requests.get(url=url)
    # data = json.loads(resp.text)
    try:
        return resp.json()['Data']
    except Exception:
        return []

