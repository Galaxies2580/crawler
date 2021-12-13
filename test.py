import requests
from lxml import etree


url = "http://192.168.129.128/pikachu-master/"
headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43"}
html = requests.get(url , headers = headers)
html.encoding='utf-8'
etree_html=etree.HTML(html.text)
content = etree_html.xpath('//*[@id="sidebar"]/ul/li/ul/li/a/text()')


for each in content:
    replace = each.replace('\n', '').replace(' ', '')
    if replace == '\n' or replace == '':
        continue
    else:
        print(replace)
