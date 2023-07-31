import requests
import json

# 双色球历史开奖数据
baseUrl = 'https://mix.lottery.sina.com.cn/gateway/index/entry'

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }

def getTwoColor(page):

    param = {
        "__caller__": "web",
        "__verno__":"1",
        "__version__":"1",
        "cat1":"gameOpenList",
        "format":"json",
        "lottoType":"101",
        "page":page,
        "paginationType":"1",
        "pageSize":"20",
        "dpc":"1"
    }
    response = requests.get(baseUrl,headers=headers,params=param)
    text = json.loads(response.text)
    return text

def saveAllData(file):
    text = getTwoColor("1")
    totalPage = int(text['result']['pagination']['totalPage'])
    totalCount = int(text['result']['pagination']['totalCount'])
    print('共计%s条数据'%(totalCount))
    print('正在写入中')

# 普通文件默认的缓冲行为，缓冲区的大小4096
    with open(file,'w') as result:
        result.write("%s\t%s\t\t\t\t%s\t\t\t%s\n"%('期数','开奖时间','红球','蓝球'))
        for i in range(1,totalPage+1):
            text = getTwoColor(i)
            datas = text['result']['data']
            for data in datas:
                result.write(data['issueNo']+'\t')
                result.write(data['openTime']+'\t')
                result.write(' '.join(str(x) for x in data['redResults'])+'\t')
                result.write(' '.join(str(x) for x in data['blueResults'])+'\t')
                result.write('\n')
    print('已保存')

def saveNewDate(file):
    text = getTwoColor("1")
    data = text['result']['data'][0]
    with open(file,'a') as result:
            result.write(data['issueNo']+'\t')
            result.write(data['openTime']+'\t')
            result.write(' '.join(str(x) for x in data['redResults'])+'\t')
            result.write(' '.join(str(x) for x in data['blueResults'])+'\t')
            result.write('\n')

if __name__ == "__main__":
    saveNewDate('text.txt')