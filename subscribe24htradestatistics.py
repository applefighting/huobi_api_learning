import logging
from huobi import SubscriptionClient
from huobi.model import *

logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

sub_client = SubscriptionClient()


# def callback(trade_statistics_event: 'TradeStatisticsEvent1'):
#     trade_statistics_event.print_object()
#     print()


# sub_client.subscribe_24h_trade_statistics_event("atomusdt", callback)

# Subscribe the trade update for btcusdt.
# def callback(trade_event: 'TradeEvent'):
#     print(trade_event.symbol)
#     for trade in trade_event.trade_list:
#         print(trade.price)

# subscription_client.subscribe_trade_event("btcusdt", callback)

#Subscribe candlestick/KLine update

def callback(candlestick_event: 'CandlestickEvent'):
    print(candlestick_event.data.high)

sub_client.subscribe_candlestick_event("btcusdt", CandlestickInterval.MIN15, callback)