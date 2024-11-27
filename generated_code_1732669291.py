Sure, here's a simple python script for range trading using Alpaca API.

```python
import alpaca_trade_api as tradeapi
import time

api = tradeapi.REST('APCA-API-KEY-ID', 'APCA-API-SECRET-KEY', base_url='https://paper-api.alpaca.markets') 

symbol = 'AAPL'
current_order = None
last_price = 1

def limit_buy(symbol, qty, limit_price):
    return api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='limit',
        time_in_force='gtc',
        limit_price=limit_price
    )

def limit_sell(symbol, qty, limit_price):
    return api.submit_order(
        symbol=symbol,
        qty=qty,
        side='sell',
        type='limit',
        time_in_force='gtc',
        limit_price=limit_price
    )

def wait_for_fill(order_id):
    while True:
        order = api.get_order(order_id)
        if order.status == 'filled':
            return order
        time.sleep(1)

def range_trade(symbol, qty, buy_price, sell_price):
    global current_order
    global last_price

    if current_order is not None:
        api.cancel_order(current_order.id)

    position = None
    try:
        position = api.get_position(symbol)
    except:
        pass

    if position is None:
        current_order = limit_buy(symbol, qty, buy_price)
        current_order = wait_for_fill(current_order.id)
        last_price = current_order.filled_avg_price
    else:
        current_order = limit_sell(symbol, position.qty, sell_price)
        current_order = wait_for_fill(current_order.id)
        last_price = current_order.filled_avg_price

while True:
    range_trade(symbol, 1, last_price * 0.99, last_price * 1.01)
    time.sleep(1)
```

Please replace `'APCA-API-KEY-ID'` and `'APCA-API-SECRET-KEY'` with your actual Alpaca API key and secret key. This script will continually range trade the specified symbol. It will buy when the price drops 1% below the last price and sell when the price rises 1% above the last price.