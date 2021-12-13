import re
import urllib
from urllib import request
from bs4 import BeautifulSoup
import threading
import time
from selenium import webdriver


# 创建一个以标题为文本名的txt文件，并记录此页面的URL
def down_str1(title, str):
    title = re.sub(r'\W', '', title)
    title = 'D:/googlepatents/' + title + '.txt'
    # print(title)
    with open(title, mode='w', encoding='utf-8') as file_obj:
        file_obj.write(str)


# 将内容写入为标题名的txt文件中
def down_str2(title, str):
    title = re.sub(r'\W', '', title)
    title = 'D:/googlepatents/' + title + '.txt'
    # print(title)
    with open(title, mode='a', encoding='utf-8') as file_obj:
        file_obj.write(str)


# 获取文本内容
def find_str(url):
    # print(url)
    time.sleep(3)  # 设置中场休息时间
    html_text = get_url_dynamic2(url)
    soup = BeautifulSoup(html_text, 'lxml')
    # htmlfile = open('test.html', 'r', encoding='utf-8')  #用本地html测试时使用
    # htmlhandle = htmlfile.read()
    # soup = BeautifulSoup(htmlhandle, 'lxml')
    soup = soup.find('div', {'id': {'wrapper'}, 'class': {'style-scope patent-result'}})
    # print(soup)
    title = soup.h1.stripped_strings #获取专利标题
    title = list(title)[0]
    # print(title)
    down_str1(title, url) #创建一个以专题标题为文件名的txt

    abstract = soup.find('div', {'abstract style-scope patent-text'}) #获取abstract的内容
    # print(list(abstract.stripped_strings))
    down_str2(title, 'abstract\n')
    if abstract.stripped_strings is not None:
        for ats in list(abstract.stripped_strings):
            down_str2(title, ats + '\n')

    description = soup.find('div', {'description style-scope patent-text'}) #获取description的内容
    # print(list(description.stripped_strings))
    down_str2(title, 'description\n')
    if description.stripped_strings is not None:
        for dns in list(description.stripped_strings):
            down_str2(title, dns + '\n')

    claims = soup.find('div', {'class': {'claims style-scope patent-text'}}) #获取claims的内容
    # print(list(claims.stripped_strings))
    down_str2(title, 'claims\n')
    if claims.stripped_strings is not None:
        for css in list(claims.stripped_strings):
            down_str2(title, css + '\n')

    print(time.ctime(time.time())) #打印完成时间
    return


# 利用本地浏览器访问url，并获取js运行之后的网页源码
def get_url_dynamic2(url):
    driver = webdriver.Chrome()  # 调用本地的火狐浏览器，Chrome 甚至 Ie 也可以的
    driver.set_page_load_timeout(15)  # 设置超时等待的时间，超过不再等待
    try:
        driver.get(url)  # 请求页面，会打开一个浏览器窗口
    except:
        driver.execute_script('window.stop()')
    html_text = driver.page_source
    driver.quit()
    # print html_text
    return html_text


# 由初始url获取初始内容，并进行利用
def getContent(urls):
    for url in urls:
        time.sleep(3)
        # print(url)
        try:
            html_text = get_url_dynamic2(url)
            soup = BeautifulSoup(html_text, 'lxml')
            # print(soup)
            m_tr = soup.find_all('article', {'class': {'result style-scope search-result-item'}}) #搜寻网页中每一个专利对应的大标签
            # print(m_tr)
            for url in m_tr:
                try:
                    url = url.find_all('state-modifier')[0].get('data-result') #从当前专利中获取进入该专利网页的URL
                    # print(m_tr)
                    url = "https://patents.glgoo.top/" + url
                    find_str(url)
                except:
                    if url == urls[len(urls) - 1]:
                        break
                    else:
                        continue
        except:
            if url == urls[len(urls) - 1]:
                break
            else:
                continue


class myThread(threading.Thread):
    def __init__(self, threadID, urls):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.urls = urls

    def run(self):
        print("thread" + self.threadID + ":start!")
        time.sleep(2)
        getContent(self.urls)
        print("thread" + self.threadID + ":exit!")


if __name__ == '__main__':
    # url = ['https://patents.glgoo.top/?q=%E5%A4%A7%E6%95%B0%E6%8D%AE&num=100&page=0',]
    # getContent(url)
    # thread = myThread("test",url)
    # thread.start()
    # thread.join()
    url = 'https://patents.glgoo.top/?q=%E5%A4%A7%E6%95%B0%E6%8D%AE&num=100&page='
    thread1 = []
    for i in range(0, 3):
        thread1.append(url + str(i))
    thread1 = myThread("1", thread1)

    thread2 = []
    for i in range(3, 6):
        thread2.append(url + str(i))
    thread2 = myThread("2", thread2)

    thread3 = []
    for i in range(6, 10):
        thread3.append(url + str(i))
    thread3 = myThread("3", thread3)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()
    print("finished!")


    #本地测试用的专利大标签
    html_text = """
        <article class="result style-scope search-result-item">
<state-modifier act='{"type": "OPEN_RESULT", "result": "$result"}' class="result-title style-scope search-result-item" data-result="patent/CN105487499B/zh"><a class="style-scope state-modifier" href="#" id="link">
<h3 class="style-scope search-result-item"><raw-html class="style-scope search-result-item">
<span class="style-scope raw-html" id="htmlContent" style="display: inline;"> 过程控制系统中的区域性<b>大数据</b></span>
</raw-html></h3>
</a></state-modifier>
<result-tags class="style-scope search-result-item"><div class="style-scope result-tags" hidden="">
<template class="style-scope result-tags" is="dom-if"></template>
</div>
</result-tags>
<div class="abstract layout horizontal start style-scope search-result-item">
<template class="style-scope search-result-item" is="dom-if"></template>
<div class="flex style-scope search-result-item">
<div class="layout horizontal start style-scope search-result-item">
<div class="figureViewButtonWrap style-scope search-result-item">
<img class="thumbnail style-scope search-result-item" src="" style="display: none;"/>
<div class="figureViewButton layout horizontal style-scope search-result-item">
<iron-icon class="style-scope search-result-item x-scope iron-icon-0" icon="icons:chevron-right"><svg class="style-scope iron-icon" focusable="false" preserveaspectratio="xMidYMid meet" style="pointer-events: none; display: block; width: 100%; height: 100%;" viewbox="0 0 24 24"><g class="style-scope iron-icon"><path class="style-scope iron-icon" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></g></svg>
</iron-icon>
</div>
</div>
<div class="flex style-scope search-result-item">
<h4 class="metadata style-scope search-result-item">
<span class="active style-scope search-result-item">US</span>
<span class="active style-scope search-result-item">CN</span>
<span class="active style-scope search-result-item">JP</span>
<span class="active style-scope search-result-item">DE</span>
<span class="active style-scope search-result-item">GB</span>
<template class="style-scope search-result-item" is="dom-repeat"></template><span class="bullet-before style-scope search-result-item">
<a class="pdfLink style-scope search-result-item" href="https://patentimages.storage.googleapis.com/bc/13/c6/da2299ec3780be/CN105487499B.pdf" target="_blank"><span class="style-scope search-result-item">CN105487499B</span></a>
<template class="style-scope search-result-item" is="dom-if"></template>
<template class="style-scope search-result-item" is="dom-if"></template>
</span><span class="style-scope search-result-item"><span class="bullet-before style-scope search-result-item"><raw-html class="style-scope search-result-item">
<span class="style-scope raw-html" id="htmlContent" style="display: inline;">P·索恩约</span>
</raw-html></span></span> <span class="style-scope search-result-item"><span class="bullet-before style-scope search-result-item"><raw-html class="style-scope search-result-item">
<span class="style-scope raw-html" id="htmlContent" style="display: inline;">费希尔-罗斯蒙特系统公司</span>
</raw-html></span></span>
</h4>
<h4 class="dates style-scope search-result-item">Priority 2014-10-06 • Filed 2015-09-30 • Granted 2020-10-23 • Published 2020-10-23</h4>
<template class="style-scope search-result-item" is="dom-if"></template>
<raw-html class="style-scope search-result-item">
<span class="style-scope raw-html" id="htmlContent" style="display: inline;"> 在过程工厂或者过程控制系统的实时操作期间，区域性<b>大数据</b>节点对该工厂/系统的多个区域中的相应区域进行监督或者服务，其中这些区域中的至少一些均包括可操作用于对在该工厂/系统中执行的过程进行控制的一个或多个过程控制设备。该区域性<b>大数据</b>节点被配置为：将流式数据以及其相应区域所生成、接收或者观测的学到的知识作为<b>大数据</b>进行接收和存储，并对所存储的数据中的至少一些执行一种或多种学习分析。作为该学习分析的结果，该区域性<b>大数据</b>节点创建新的学到的知识，其中该区域性<b>大数据</b>节点可以利用该新的学到的知识来修改其相应区域中的操作，和/或该区域性<b>大数据</b>节点可以向该工厂/系统的其它<b>大数据</b>节点发送该新的学到的知识。</span>
</raw-html>
</div>
<search-result-entities class="style-scope search-result-item">
<div class="style-scope search-result-entities" id="entities">
<template class="style-scope search-result-entities" is="dom-repeat"></template>
</div>
</search-result-entities>
<template class="style-scope search-result-item" is="dom-if"></template>
</div>
<template class="style-scope search-result-item" is="dom-if"></template>
</div>
<template class="style-scope search-result-item" is="dom-if"></template>
</div>
</article>
        """
