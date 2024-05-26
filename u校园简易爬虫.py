from lxml import etree
from collections import OrderedDict
import random
import requests
import json
from 语音识别 import dddd
url = 'https://uexercise.unipus.cn/itest/s/clsanswer/load'
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Length": "16",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": '**',
    "Host": "uexercise.unipus.cn",
    "Origin": "https://uexercise.unipus.cn",
    "Referer": "**",
    "Sec-Ch-Ua": "\"Chromium\";v=\"124\", \"Microsoft Edge\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "**",
    "X-Requested-With": "XMLHttpRequest"
}


data = {'dataid': '157032832'}

response = requests.post(url, headers=headers, data=data)
data = json.loads(response.text)

data = data['data']['C_HTML']

# 解析 HTML
parser = etree.HTMLParser()
tree = etree.fromstring(data, parser)

result = tree.xpath('//div[@class="itest-hear-reslist"]/span/text()')
choose = tree.xpath('//div[@class="option hear-row"]/label/text()')

# 选择位于同一 <p> 元素内的文本和粗体文本
text_and_bold_text = tree.xpath('//p[@style="text-align:justify"]/text() | //p[@style="text-align:justify"]/b/text()')

# 输出文本和粗体文本
# 将列表转换为单个字符串
text_string = ''.join(text_and_bold_text)

print('选择题全部为：')
for i in choose:
    print(i)
print('填空题为：')
print(text_string)

sum = 0
for i in result:
    sum += 1
    i = eval(i)

    url_list = []
    for item in i:
        if item.startswith("https"):
            url_list.append(item)
            unique_urls = OrderedDict.fromkeys(url_list)
            i = random.randint(1, 10000)
            for url in unique_urls:
                r = requests.get(url)
            #这里换成你自己的地址
            with open(str(sum) + r".mp3", 'ab') as f:
                f.write(r.content)
    print('第' + str(sum) + '部分听力为')
    dddd(str(sum) + '.mp3')

print('结束了！')
