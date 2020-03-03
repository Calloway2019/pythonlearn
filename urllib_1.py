from urllib import request

url = "http://www.dianping.com"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}
req = request.Request(url,headers= header)
res = request.urlopen(req)

print(res.geturl())
print(res.getcode())
print(res.info())

# html = res.read()
# html.decode("utf-8")

# print(html)
