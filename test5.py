from urllib import request
import urllib
from io import BytesIO
import gzip
import dryscrape
class Spilder():
    #斗鱼url
    url='https://www.cnipa.gov.cn/jsearchfront/search.do?websiteid=100000000000000&searchid=25&pg=&total=&p=1&tpl=20&q=%E5%A4%A7%E6%95%B0%E6%8D%AE&pq=&oq=&eq=&pos=&sortFields=&begin=20180102&end=20180102'


    def __fetch_content(self):
        header = {
            "Host": "www.cnipa.gov.cn",
            "Connection": "close",
            "Cache-Control": "max-age=0",
            "sec-ch-ua": '"Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "DNT": "1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer":"https://www.cnipa.gov.cn/jsearchfront/search.do?websiteid=100000000000000&searchid=25&pg=&total=&p=1&tpl=20&q=%E5%A4%A7%E6%95%B0%E6%8D%AE&pq=&oq=&eq=&pos=&sortFields=&begin=20180101&end=20180101",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cookie": "user_sid=7333e55caace49a89acdc8fc707be99a; _city=%E6%B8%A9%E5%B7%9E%E5%B8%82; JSESSIONID=7AF9C34F429AAC24E59B29D0170115B5; searchsign=802a9321ffca4e55a09c3e30a411722c; _trs_uv=kwkl4777_4693_dxgj; _q=%u5927%u6570%u636E%3A; _va_ref=%5B%22%22%2C%22%22%2C1639228859%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _va_ses=*; _trs_ua_s_1=kx1ujftp_4693_5hyt; _va_id=fa46f1023e844695.1638185108.5.1639229649.1639224850.",
        }
        response = urllib.request.Request(url = Spilder.url, headers = header)
        r = request.urlopen(response)
        # htmls = r.getcode()
        htmls = r.read()
        buff = BytesIO(htmls)
        f = gzip.GzipFile(fileobj=buff)
        htmls = f.read().decode('utf-8')
        print(htmls)

    def go(self):
        self.__fetch_content()

spilder=Spilder()
spilder.go()
