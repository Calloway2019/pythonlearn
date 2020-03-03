import requests
from bs4 import BeautifulSoup

url = "http://wsjkw.sc.gov.cn/scwsjkw/gzbd/fyzt.shtml"

res = requests.get(url)
res.encoding = "utf-8"
html = res.text
Bs = BeautifulSoup(html)
a = Bs.find("a")
p = Bs.find("p")
# print(a.attrs)
# print(a.attrs["href"])

url_new = "http://wsjkw.sc.gov.cn" + a.attrs["href"]

res = requests.get(url_new)
res.encoding = "utf-8"
html_2 = res.text
Bs_2 = BeautifulSoup(html_2)
p = Bs_2.find("p")
print(p)
