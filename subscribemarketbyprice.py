import logging
from huobi import SubscriptionClient
from huobi.model import *

logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

sub_client = SubscriptionClient()

def callback(trade_event: 'TradeEvent'):
    print(trade_event.symbol)
    for trade in trade_event.trade_list:
        print(trade.direction)
        print(trade.price)
        print(trade.amount)

def error_handler(e: 'HuobiApiException'):
    print(e.error_code)
    print(e.error_message)

sub_client.subscribe_trade_event("ltcusdt", callback, error_handler)

#sub_client.subscribe_trade_event("btcusdt", callback)