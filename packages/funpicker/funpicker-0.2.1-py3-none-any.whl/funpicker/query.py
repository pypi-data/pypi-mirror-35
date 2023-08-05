import ccxt
import cryptocompare
from enum import Enum
from funpicker.price import get_historical_price, get_price
from funpicker.orderbook import get_orderbook


class QueryTypes(Enum):
    historical = 1
    price = 2
    orderbook = 3
    sentiment = 4 # this is a placeholder for the next step


class Query:
    def __init__(self):
        """Query uses a FIFO queue to determine what"""
        self.crypto = "BTC"
        self.curr="USD"
        self.exchange='CCCAGG'
        self.period="minute"
        self.limit=1400
    
    def set_crypto(self, crypto, curr="USD", exchange='CCCAGG', period="minute", limit=1400, queue=False):
        """Set the main cryptocurrency for this function"""
        self.crypto = crypto
        return self

    def set_fiat(self, fiat="USD"):
        """Set the main fiat or trade pair for cryptocurrency. It can be abother crypto. Using fiat for now."""
        self.curr = fiat
        return self

    def set_exchange(self, exchange):
        """Set the exchange"""
        self.exchange = exchange
        return self

    def set_period(self, period):
        """Set the period"""
        self.period = period
        return self

    def set_limit(self, limit=1500):
        """Set the limit"""
        self.limit = limit
        return self

    def get(self, qt=QueryTypes.historical):
        """Get the information you're requesting."""
        if qt == QueryTypes.historical:
            return get_historical_price(self.crypto, curr=self.curr, exchange=self.exchange, period=self.period, limit=self.limit)
        elif qt == QueryTypes.price:
            return get_price(self.crypto, curr=self.curr, exchange=self.exchange)
        elif qt == QueryTypes.orderbook:
            if self.exchange != 'CCCAGG':
                return get_orderbook(self.crypto, self.curr, exchange=self.exchange)
            else:
                return get_orderbook(self.crypto, self.curr)
        # check to get the orderbook
            # Get it from ccxt
            # Check for the errors
        # elif qt == QueryTypes:
