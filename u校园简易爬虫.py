from lxml import etree
from collections import OrderedDict
import random
import requests
import json

url = 'https://uexercise.unipus.cn/itest/s/clsanswer/load'
headers = {
    'User-Agent': '**',
    'Cookie': '**',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://uexercise.unipus.cn',
    'Referer': 'https://uexercise.unipus.cn/uexercise/api/v1/enter_exercise_exam?plf=0&schoolId=9679&openId=9909d1a186744fa290913c14f339714c&studentId=18762866&exerciseId=3966849&exerciseType=2&clazzId=820479&forwardUrl=https%3A%2F%2Fu.unipus.cn%2Fuser%2Fstudent%2Fhomework%2Findex%3FcourseId%3D1290%26school_id%3D9679%26type%3D2%26eccId%3D112849%26classId%3D820479%26activationStatus%3D1&sign=70495f0cc34f49b7b2e60d20db23974b',
}

data = {'dataid': '157032832'}

response = requests.post(url, headers=headers, data=data)
data = json.loads(response.text)

data = data['data']['C_HTML']
# 解析 HTML
parser = etree.HTMLParser()
tree = etree.fromstring(data, parser)

result = tree.xpath('//div[@class="itest-hear-reslist"]/span/text()')
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
            with open(r"C:\Users\Administrator\Desktop\u\\"+str(sum) + r".mp3", 'ab') as f:
                f.write(r.content)
print('结束了！')

