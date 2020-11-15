import requests
import json

url = 'https://api.huobi.pro/general/exchange_rate/list'
r = requests.get(url)

print('status code:', r.status_code)

response_dict = r.json()

# print ('Total rates:', response_dict['total_count'])

repo_dicts = response_dict['data']
coinpairs = []
pairrates = []
for pairs in repo_dicts:
    p = pairs['name']
    coinpairs.append(p)
    r = pairs['rate']
    pairrates.append(r)
    
rate_dict = dict(zip(coinpairs,pairrates))

# basecoin = input('请输入基础货币:')
# quotecoin = input ('请输入计价货币:')

# get_pair = basecoin + "_" + quotecoin

# if get_pair in coinpairs:
#     print(get_pair,"Rate:",rate_dict[get_pair])
# else:
#     print('无该币对')

filename = 'huobi_rates.json'
with open (filename,'w') as f:
    json.dump(rate_dict,f)

# print('usd_mdl:',rate_dict['usd_mdl'])
# print('Total rate:', len(repo_dicts))
# repo_dict = repo_dicts[0]
# print ('\nKeys:', len(repo_dict))

# for key in sorted(repo_dict.keys()):
#     print(key)

# print ('Pairs:', repo_dict['name'])
# print ('Rate:', repo_dict['rate'])