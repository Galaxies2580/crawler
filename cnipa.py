import re
import urllib
from urllib import request
from bs4 import BeautifulSoup
import threading
import time
from selenium import webdriver
#将文本内容进行下载，并利用url名字命名文本
def down_str(title,str):
    # title = re.sub(r'.*/','',urlname)
    # title = re.sub(r'\..*','',title)
    title = re.sub(r'\W','',title)
    title = 'D:/cnipa/'+title+'.txt'
    print(title)
    with open(title, mode='w', encoding='utf-8') as file_obj:
        file_obj.write(str)
#获取文本内容
def find_str(url):
    time.sleep(10) #设置中场休息时间
    html_text = get_url_dynamic2(url)
    soup = BeautifulSoup(html_text,'lxml')

    title = soup.h1.text
    # print(title)
    # print(soup)
    find_ss = soup.find_all('div',{'class':{'article-content cont'}})
    # print(list(find_ss[0].stripped_strings))
    if len(find_ss) > 0 :
        find_s = find_ss[0]
        str = url+'\n'
        for sstr in list(find_s.stripped_strings):
            str = str + sstr.replace(' ','').replace('\n','')
        print(str)
        down_str(title,str)
    print(time.ctime(time.time()))
    return

# 获取网页中的url
def find_url(str):
    a_list = []
    find_s = str.find_all('ul',{'class':{'submenu'}})
    for v in find_s:
        for a in v.find_all('a'):
            #print(a['href'])
            a_list.append(a['href'])
    #print(a_list)
    return a_list

#利用本地浏览器访问url，并获取js运行之后的网页源码
def get_url_dynamic2(url):
    driver=webdriver.Chrome() #调用本地的火狐浏览器，Chrom 甚至 Ie 也可以的
    driver.set_page_load_timeout(10) #设置超时等待的时间，超过不再等待
    try:
        driver.get(url) #请求页面，会打开一个浏览器窗口
    except:
        driver.execute_script('window.stop()')
    html_text=driver.page_source
    driver.quit()
    #print html_text
    return html_text


# 由初始url获取初始内容，并进行利用
def getContent(urls):
    for url in urls:
        time.sleep(10)
        # print(url)
        html_text = get_url_dynamic2(url)
        soup = BeautifulSoup(html_text,'lxml')
        # print(soup)
        m_tr = soup.find_all('div',{'class':{'jcse-news-url'}})
        # print(m_tr)
        # print(m_tr[0].a.text)
        # find_str(m_tr[0].a.text)
        for url in m_tr:
            url = url.a.text
            # print(url)
            find_str(url)

class myThread(threading.Thread):
    def __init__(self,threadID,urls):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.urls = urls
    def run(self):
        print("thread"+self.threadID+":start!")
        getContent(self.urls)
        print("thread"+self.threadID+":exit!")

if __name__ == '__main__':
#     url = 'https://www.cnipa.gov.cn/jsearchfront/search.do?websiteid=100000000000000&/searchid=25&pg=&total=&p=1&tpl=2\
# 0&q=%E5%A4%A7%E6%95%B0%E6%8D%AE&pq=&oq=&eq=&pos=&sortFields=&begin=20180101&end=20180101'
    # getContent('https://www.cnipa.gov.cn/jsearchfront/search.do?websiteid=100000000000000&searchid=25&pg=&total=&p=1&tpl=20&q=%E5%A4%A7%E6%95%B0%E6%8D%AE&pq=&oq=&eq=&pos=&sortFields=&begin=20180102&end=20180102')
    thread1 = []
    for m in range(1,13):
        strm = ''
        if m < 10 :
            strm = '0' + str(m)
        else:
            strm = str(m)
        for d in range(1,32,5):
            strd = ''
            if d < 10:
                strd = strm + '0' + str(d)
            else:
                strd = strm + str(d)
            # print(strd)
            url = 'https://www.cnipa.gov.cn/jsearchfront/search.do?websiteid=100000000000000&/searchid=25&pg=&total=&p=1&tpl=2\
0&q=%E5%A4%A7%E6%95%B0%E6%8D%AE&pq=&oq=&eq=&pos=&sortFields=&begin=2018'+strd+'&end=2018'+strd
            # print(url)
            thread1.append(url)
    # print(thread1)
    thread2 = []
    for m in range(1,13):
        strm = ''
        if m < 10 :
            strm = '0' + str(m)
        else:
            strm = str(m)
        for d in range(2,31,5):
            strd = ''
            if d < 10:
                strd = strm + '0' + str(d)
            else:
                strd = strm + str(d)
            # print(strd)
            url = 'https://www.cnipa.gov.cn/jsearchfront/search.do?websiteid=100000000000000&/searchid=25&pg=&total=&p=1&tpl=2\
0&q=%E5%A4%A7%E6%95%B0%E6%8D%AE&pq=&oq=&eq=&pos=&sortFields=&begin=2018'+strd+'&end=2018'+strd
            # print(url)
            thread2.append(url)
    thread3 = []
    for m in range(1,13):
        strm = ''
        if m < 10 :
            strm = '0' + str(m)
        else:
            strm = str(m)
        for d in range(3,31,5):
            strd = ''
            if d < 10:
                strd = strm + '0' + str(d)
            else:
                strd = strm + str(d)
            # print(strd)
            url = 'https://www.cnipa.gov.cn/jsearchfront/search.do?websiteid=100000000000000&/searchid=25&pg=&total=&p=1&tpl=2\
0&q=%E5%A4%A7%E6%95%B0%E6%8D%AE&pq=&oq=&eq=&pos=&sortFields=&begin=2018'+strd+'&end=2018'+strd
            # print(url)
            thread3.append(url)
    thread4 = []
    for m in range(1,13):
        strm = ''
        if m < 10 :
            strm = '0' + str(m)
        else:
            strm = str(m)
        for d in range(4,31,5):
            strd = ''
            if d < 10:
                strd = strm + '0' + str(d)
            else:
                strd = strm + str(d)
            # print(strd)
            url = 'https://www.cnipa.gov.cn/jsearchfront/search.do?websiteid=100000000000000&/searchid=25&pg=&total=&p=1&tpl=2\
0&q=%E5%A4%A7%E6%95%B0%E6%8D%AE&pq=&oq=&eq=&pos=&sortFields=&begin=2018'+strd+'&end=2018'+strd
            # print(url)
            thread4.append(url)
    thread5 = []
    for m in range(1,13):
        strm = ''
        if m < 10 :
            strm = '0' + str(m)
        else:
            strm = str(m)
        for d in range(5,31,5):
            strd = ''
            if d < 10:
                strd = strm + '0' + str(d)
            else:
                strd = strm + str(d)
            # print(strd)
            url = 'https://www.cnipa.gov.cn/jsearchfront/search.do?websiteid=100000000000000&/searchid=25&pg=&total=&p=1&tpl=2\
0&q=%E5%A4%A7%E6%95%B0%E6%8D%AE&pq=&oq=&eq=&pos=&sortFields=&begin=2018'+strd+'&end=2018'+strd
            # print(url)
            thread5.append(url)
    thread1 = myThread("1",thread1)
    thread2 = myThread("2",thread2)
    thread3 = myThread("3",thread3)
    thread4 = myThread("4",thread4)
    thread5 = myThread("5",thread5)
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    print("finished!")