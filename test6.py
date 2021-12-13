from selenium import webdriver

def get_url_dynamic2(url):
    driver=webdriver.Chrome() #调用本地的火狐浏览器，Chrom 甚至 Ie 也可以的
    driver.get(url) #请求页面，会打开一个浏览器窗口
    html_text=driver.page_source
    driver.quit()
    #print html_text
    return html_text
url='https://www.cnipa.gov.cn/jsearchfront/search.do?websiteid=100000000000000&searchid=25&pg=&total=&p=1&tpl=20&q=%E5%A4%A7%E6%95%B0%E6%8D%AE&pq=&oq=&eq=&pos=&sortFields=&begin=20180102&end=20180102'
print(get_url_dynamic2(url)) #将输出一条文本