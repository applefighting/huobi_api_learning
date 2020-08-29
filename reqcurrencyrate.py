import requests
import json

# url = 'https://hashscape.com/tx/3d59bbe821fbc179b5d4c4a8e0d1e305dc3e64178a9b74f684d71d6b488a3956'
# req = requests.get(url)

with open ('tx.json','r') as f:
   # tx_requests = f.write(req.text)
   tx_info = json.load(f)




print(tx_info)
# currency = input('请输入货币:')
# if currency.upper in currency_list:
#     print("1 USD can change:")
#     print(currency_list[currency])
#     # print(currency)
# else:
#     print('货币不存在')