import json

#While True打头的循环可以不断运行
while True:
    #输入要查询币对的基础货币或者退出程序
    basecoin = input('请输入基础货币,退出输入quit:')

    #判断是否退出程序
    if basecoin == 'quit':
        break

    #输入币对的计价货币
    quotecoin = input ('请输入计价货币:')

    #将用户的输入拼成币对，便于查询
    get_pair = basecoin + "_" + quotecoin

    #打开之前写下的文件，将内存存储到变量中
    filename = 'huobi_rates.json'
    with open (filename) as f:
        rate_dict = json.load(f)

    #判断币对是否存在
    if get_pair in rate_dict.keys():
        #存在就打印币对键对应的汇率值
        print(get_pair,"Rate:",rate_dict[get_pair])
    #不存在就打印无币对
    else:
        print('无该币对')

