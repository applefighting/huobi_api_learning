from huobi import RequestClient

request_client = RequestClient()

# Get the timestamp from Huobi server and print on console
timestamp = request_client.get_exchange_timestamp()
print(timestamp)

