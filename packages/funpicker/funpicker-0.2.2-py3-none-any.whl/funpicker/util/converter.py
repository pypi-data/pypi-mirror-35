def convert_usd(exchange):
    """Determine if USDT or not"""
    word = exchange.lower()
    to_usdt_list =  ["BitTrex", "binance", "Huobi", "OKEx", "Coinbene", "Digifinex", "HitBTC", "CoinEx", "ABCC", "Poloniex", "Kucoin", "Kraken"]
    low = [x.lower() for x in to_usdt_list]

    if word in low:
        return "USDT"
    return "USD"