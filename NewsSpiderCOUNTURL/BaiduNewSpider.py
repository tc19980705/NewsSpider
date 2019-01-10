# -*- coding: utf-8 -*-

import requests
from lxml import etree
import time

BaseUrl = "http://news.baidu.com/ns?word=%s&bt=%s&et=%s&tn=newstitle"

MaxSearchSize = 500

class BaiduNewSpider(object):

    def __init__(self, keyWord, header, startTime, stopTime, dataBase=None):
        super().__init__()

        self.keyWord = keyWord
        self.header = header
        self.database = dataBase
        self.startTime = time.mktime(time.strptime(startTime, "%Y-%m-%d %H:%M:%S"))
        self.stopTime = time.mktime(time.strptime(stopTime, "%Y-%m-%d %H:%M:%S"))
        self.urls = []

    def searchSize(html):
        try:
            tree = etree.HTML(html)
            tempResult = tree.xpath('//span[@class="nums"]/text()')[0]

            if tempResult[6].isdigit():
                temp = tempResult[6: -1]
                temp = int(temp.replace(",", ""))
                print(temp)
            else:
                temp = tempResult[7: -1]
                temp = int(temp.replace(",", ""))
                print(temp)
            return temp
        except Exception as e:
            raise e
            
    def makeUrls(keyWord, startTime, stopTime, headers):
        searchUrls = []
        url = BaseUrl % (keyWord, str(startTime), str(stopTime))
        
        print(url)

        html = requests.get(url, headers=headers).text
        time.sleep(1)
        if BaiduNewSpider.searchSize(html) > MaxSearchSize:
            medainTime = (stopTime + startTime) / 2
            
            searchUrls.append(BaiduNewSpider.makeUrls(keyWord, startTime, medainTime, headers))
            searchUrls.append(BaiduNewSpider.makeUrls(keyWord, medainTime, stopTime, headers))
        else:
            searchUrls.append(url)
        
        return searchUrls

def flat(nums):
    res = []
    for i in nums:
        if isinstance(i, list):
            res.extend(flat(i))
        else:
            res.append(i)
    return res
        

if __name__ == "__main__":
    headers = {
        'Host': 'news.baidu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36\
         (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
    }
    keyword = u"权健"

    search = BaiduNewSpider(
        keyword,
        headers,
        "2016-01-01 00:00:00",
        "2019-01-08 00:00:00"
    )
    
    search.urls.append(BaiduNewSpider.makeUrls(search.keyWord, search.startTime, search.stopTime, search.header))

    fullResult = flat(search.urls)
    print(fullResult)
