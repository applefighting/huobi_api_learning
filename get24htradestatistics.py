from huobi import RequestClient

request_client = RequestClient()

# symbol_list = ["btcusdt"]
# for symbol_row in symbol_list:
#     trade_statistics = request_client.get_24h_trade_statistics(symbol_row)
#     print("---- Statistics ----")
#     trade_statistics.print_object()

trade = request_client.get_last_trade("btcusdt")
print(trade.price)