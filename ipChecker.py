import requests

kv = {'user-agent': 'Mozilla/5.0'}

url = "https://m.ip138.com/iplookup.asp?ip="
try:
    r = requests.get(url + '212.204.80.112', headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[2461:2500])
except:
    print("FAILED")
