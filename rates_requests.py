import requests
import json

url = 'https://api.huobi.pro/general/exchange_rate/list'
r = requests.get(url)

#显示接口请求状态码
print('status code:', r.status_code)

#将API相应存储在一个变量中
response_dict = r.json()

#将汇率相关的汇率的数据提取出来
repo_dicts = response_dict['data']

#分别创建一个币对和汇率的空列表
coinpairs = []
pairrates = []

#将字典中的币对和汇率值分别添加到列表中
for pairs in repo_dicts:
    p = pairs['name']
    coinpairs.append(p)
    r = pairs['rate']
    pairrates.append(r)

#将两个列表合并为一个字典，币对为键汇率为值    
rate_dict = dict(zip(coinpairs,pairrates))

#创建一个json文件，将创建的汇率字典存储下来
filename = 'huobi_rates.json'
with open (filename,'w') as f:
    json.dump(rate_dict,f)
