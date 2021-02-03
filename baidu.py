import requests

keyword = "Python"
try:
    kv = {'wd': 'Python'}
    r = requests.get("http://www.baidu.com/s", params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")

try:
    kv2 = {'q': 'Python'}
    r = requests.get("http://www.so.com/s", params=kv2)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")