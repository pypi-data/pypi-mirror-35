# Funpicker - A way of collecting price information for your trading bot.
 


`Funpicker` is a library funguana created to get the price information for exchanges. This relies most on the cryptocompare api. However, there are parts that use ccxt to pull exchange specific information.

This library is to make our application highly modular. The basic premise of it is very simple: 

1. You explain which information you want to collect in a context
2. You get a return with that information
3. You store what you intend using another library (such as `funtime` or sql)

**Understand `funpicker` is a firm wrapper around `ccxt` and `request`. Its job is to make pricing easier to access for the common bot maker**


## What makes `funpicker` better?
The single thing that makes funpicker better than all other platforms is that it relies 100% on making the process simipler for the user. There's only a couple of functions to be able to start getting information from exchanges immediately for either storage or analytics:

It is a layer on top of `request` and `ccxt`. We added the following:

* An easy way to find data
* The user will have easy query options to get data with extra grainularity
* Easy access to orderbook information. Has an option of an in-memory queue to deal with rate limits. Or you could let it fail and not acknowledge it.


## How does it work?
Using a few functions, we reach out to various API's to do the following:

* Get orderbook information
* Get pricing

In the future the plan is to introduce the following:

* General sentiment data
* Generic Twitter Streams
* Generic Reddit Streams



### Example:
---
```python
from funpicker import Queuy # this is the main query object

# Initialize the query class. 
# It has a lot of default values at the start that we could use
fpq = Query()

# This gets all of the minutely historical price information for bitcoin.
# This should work out the box
initial = fpq.get()

```


### Setting Desired Parameters dynamically
```python
from funpicker import Query, QueryType

# Now this gets the last 30 hours of ETH to USD prices. 
# This is in price format and this should be return all of the compressed candlebars
fpq = Query().set_crypto("ETH").set_fiat("USD").set_exchange("binance").set_period("hour").set_limit(30).get()
```

### Can directly get the single price data as well dynamically from an exchange. 
This price information is entirely. It has all of the information availble to send directly into `funtime`. The time-series database

```python
from funpicker import Query, QueryType

# Same as before. Only it gets the latest price information for one period of time. 
# This should be within 30-40 seconds of getting posted onto the exchange according to cryptocompare
fpq = Query().set_crypto("ETH").set_fiat("USD").set_exchange("binance").set_period("hour").set_limit(30).get(QueryType.price)
```


### Get the order book

As a data scientist, you may want to handle your data in dataframe format. With `funtime`, you can get your timestamp information in both `pandas.DataFrame` and `dask.DataFrame` format. You would use the `Converter` import. 

```python
from funpicker import Query, QueryType

# Similar as before, only it gets the orderbook when returned
fpq = Query().set_crypto("ETH").set_fiat("USD").set_exchange("binance").get(QueryType.orderbook)
```



## How to install

This requires an internet connection. Using `pip` or `pipenv`, run:


```
pip install funpicker
```

Or you can use `pipenv` for it:

```
pipenv install funpicker
```
