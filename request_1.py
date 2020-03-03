import requests

url = "http://www.dianping.com"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}
res = requests.get(url, headers = header )

print(res.encoding)
print(res.headers)
print(res.url)

res.encoding = "utf-8"
print(res.text)