import requests

def getBdMsg(keyword):
    #header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"}
    url = "https://www.baidu.com/s?wd={}".format(keyword)   

    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}
    res = requests.get( url, headers = header).text

    return res

if __name__ == "__main__":
    word = input("请输入你要搜索的页面：")
    print(getBdMsg(word))
