import re
import urllib
from urllib import request
from bs4 import BeautifulSoup
import threading
import time
#将文本内容进行下载，并利用url名字命名文本
def down_str(urlname,str):
    file_path = re.sub(r'.*/','',urlname)
    file_path = re.sub(r'\..*','',file_path)
    file_path = 'D:/OSINT/'+file_path+'.txt'
    print(file_path)
    with open(file_path, mode='w', encoding='utf-8') as file_obj:
        file_obj.write(str)
#获取文本内容
def find_str(url):
    time.sleep(5) #设置中场休息时间
    header = {
        #"Host": "yjs.cqupt.edu.cn",
        "Connection": "close",
        "Cache-Control": "max-age=0",
        "sec-ch-ua": '"Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cookie": "vvjcgVbcZbczO=5YGy_OHYjmREEOc_rWgHNx4cpMWwiD56bqKydPVFUgtgzWTjWzHjB8YHBpvLxvegb1IGNXZcwjxEuQ30y27OBpG; vvjcgVbcZbczS=5JoeZ_lbxru9dKQTVlgzAMFE2RWReRNLhyXZKk.F5qmWwANS3jiVKx3jSQo.7eSYG89mUYQyXgxNWlUs4ZhRhsa; mLvnBZTNP4mtO=5mBABNs1bHlS0MdQUubqNqbnh7JTRXObEfiUHguGJvbchYx.AKG8mnbJKouLvdEFraOTo8v0asqzULILC0U1KUG; mLvnBZTNP4mtS=5jMJgeHwJ.9rwnCkC0ek8tPYJ64Z9U4_d5_e_XinDBs3djuTERv4QpFrE6PHWb5G9K7aozcITDtoSTfkzLpErKG; UM_distinctid=17d66e5e052a42-09f5fc871ec576-5919135e-154ac4-17d66e5e0531344; JSESSIONID=50F9A7AEDAFA5D75EC161FB13CEB4C75; mLvnBZTNP4mtP=53McnmDDa7v9qqqmebO4rsGq0.Ir7YGeaQ_zFBy0fz0K72XhASyp6BwLDfoSyfyj7gbDb6_Tb7Q.9f7ODcvpC3mMxTAjt6zgNay4okjIzt9dVu5H4ohlsLk3UUlKy6q9in6bauisRmf6DNJLPuFvfJ1MEO5Mu86GE_XcaHwM1uFINbAdmoiDXBwq5INSaJA_PBxb_hrO7pkD7PJVd02Lgw_tg1COEQhKjsHkDmbN9zJvXUCfD43vKXMYtMPFQIKOMcLJbqyeeu3M1K_EJAPyIK0uvJ2PQlHuca73Snu0dmKfjfsE2RATKMp6GZ2e4kStsYsME3NQJ5ZFipxRb1Jn_8rXnGIySaGgIUooqcX_p4Q4G",
    }
    response = urllib.request.Request(url = url, headers = header)
    html_text = request.urlopen(response).read().decode('utf-8')
    soup = BeautifulSoup(html_text,'lxml')
    #print(soup)
    find_ss = soup.find_all('div',{'class':{'page-content'}})
    if len(find_ss) > 0 :
        find_s = find_ss[0]
        str = ""
        for sstr in list(find_s.stripped_strings):
            str = str + sstr.replace(' ','').replace('\n','')
        # print(str)
        down_str(url,str)
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

# 由初始url获取初始内容，并进行利用
def getContent(url):
    header = {
        #"Host": "yjs.cqupt.edu.cn",
        "Connection": "close",
        "Cache-Control": "max-age=0",
        "sec-ch-ua": '"Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cookie": "vvjcgVbcZbczO=5YGy_OHYjmREEOc_rWgHNx4cpMWwiD56bqKydPVFUgtgzWTjWzHjB8YHBpvLxvegb1IGNXZcwjxEuQ30y27OBpG; vvjcgVbcZbczS=5JoeZ_lbxru9dKQTVlgzAMFE2RWReRNLhyXZKk.F5qmWwANS3jiVKx3jSQo.7eSYG89mUYQyXgxNWlUs4ZhRhsa; mLvnBZTNP4mtO=5mBABNs1bHlS0MdQUubqNqbnh7JTRXObEfiUHguGJvbchYx.AKG8mnbJKouLvdEFraOTo8v0asqzULILC0U1KUG; mLvnBZTNP4mtS=5jMJgeHwJ.9rwnCkC0ek8tPYJ64Z9U4_d5_e_XinDBs3djuTERv4QpFrE6PHWb5G9K7aozcITDtoSTfkzLpErKG; UM_distinctid=17d66e5e052a42-09f5fc871ec576-5919135e-154ac4-17d66e5e0531344; JSESSIONID=50F9A7AEDAFA5D75EC161FB13CEB4C75; mLvnBZTNP4mtP=53McnmDDa7v9qqqmebO4rsGq0.Ir7YGeaQ_zFBy0fz0K72XhASyp6BwLDfoSyfyj7gbDb6_Tb7Q.9f7ODcvpC3mMxTAjt6zgNay4okjIzt9dVu5H4ohlsLk3UUlKy6q9in6bauisRmf6DNJLPuFvfJ1MEO5Mu86GE_XcaHwM1uFINbAdmoiDXBwq5INSaJA_PBxb_hrO7pkD7PJVd02Lgw_tg1COEQhKjsHkDmbN9zJvXUCfD43vKXMYtMPFQIKOMcLJbqyeeu3M1K_EJAPyIK0uvJ2PQlHuca73Snu0dmKfjfsE2RATKMp6GZ2e4kStsYsME3NQJ5ZFipxRb1Jn_8rXnGIySaGgIUooqcX_p4Q4G",
    }
    response = urllib.request.Request(url = url, headers = header)
    html_text = request.urlopen(response).read().decode('utf-8')
    soup = BeautifulSoup(html_text,'lxml')
    m_tr = soup.find_all('ul',{'class':{'nav nav-list'}})
    #print(m_tr)
    for url in find_url(m_tr[0]):
        url = "http://192.168.129.128/pikachu-master/" + url
        # print(url)
        find_str(url)

class myThread(threading.Thread):
    def __init__(self,threadID,url):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.url = url
    def run(self):
        print("thread"+self.threadID+":start!")
        getContent(self.url)
        print("thread"+self.threadID+":exit!")

if __name__ == '__main__':
    thread1 = myThread("1",'http://192.168.129.128/pikachu-master/index.php')
    # getContent('http://192.168.129.128/pikachu-master/index.php')
    thread1.start()
    thread1.join()
    print("finished!")