# coding:utf-8
import urllib
from urllib import request

urls = "http://192.168.129.128/pikachu-master/"
header = {
"Host": "yjs.cqupt.edu.cn",
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
response = urllib.request.Request(url = urls, headers = header)
html = request.urlopen(response).read()
html = html.decode('utf-8')  # 对二进制码进行解码
print(html)
