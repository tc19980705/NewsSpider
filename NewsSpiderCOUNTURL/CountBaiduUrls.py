# -*- coding: utf-8 -*-

import requests
from lxml import etree
import time

class CountBaiduUrls(object):
    def __init__(self, fullResult, headers=None):
        self.headers = headers
        self.fullResult = ['http://news.baidu.com/ns?word=重庆公交车坠江&bt=1538323200.0&et=1540461600.0', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540461600.0&et=1540595250.0', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540595250.0&et=1540662075.0', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540662075.0&et=1540695487.5', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540695487.5&et=1540703840.625', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540703840.625&et=1540708017.1875', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540708017.1875&et=1540712193.75', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540712193.75&et=1540720546.875', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540720546.875&et=1540724723.4375', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540724723.4375&et=1540728900.0', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540728900.0&et=1540745606.25', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540745606.25&et=1540762312.5', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540762312.5&et=1540770665.625', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540770665.625&et=1540774842.1875', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540774842.1875&et=1540779018.75', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540779018.75&et=1540787371.875', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540787371.875&et=1540795725.0', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540795725.0&et=1540804078.125', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540804078.125&et=1540812431.25', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540812431.25&et=1540829137.5', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540829137.5&et=1540845843.75', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540845843.75&et=1540854196.875', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540854196.875&et=1540858373.4375', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540858373.4375&et=1540862550.0', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540862550.0&et=1540870903.125', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540870903.125&et=1540879256.25', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540879256.25&et=1540887609.375', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540887609.375&et=1540895962.5', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540895962.5&et=1540929375.0', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540929375.0&et=1540946081.25', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540946081.25&et=1540962787.5', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540962787.5&et=1540996200.0', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1540996200.0&et=1541029612.5', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1541029612.5&et=1541037965.625', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1541037965.625&et=1541046318.75', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1541046318.75&et=1541063025.0', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1541063025.0&et=1541096437.5', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1541096437.5&et=1541113143.75', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1541113143.75&et=1541121496.875', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1541121496.875&et=1541125673.4375', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1541125673.4375&et=1541129850.0', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1541129850.0&et=1541134026.5625', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1541134026.5625&et=1541138203.125', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1541138203.125&et=1541146556.25', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1541146556.25&et=1541154909.375', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1541154909.375&et=1541163262.5', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1541163262.5&et=1541196675.0', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1541196675.0&et=1541213381.25', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1541213381.25&et=1541230087.5', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1541230087.5&et=1541263500.0', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1541263500.0&et=1541397150.0', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1541397150.0&et=1541530800.0', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1541530800.0&et=1541564212.5', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1541564212.5&et=1541597625.0', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1541597625.0&et=1541664450.0', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1541664450.0&et=1541798100.0', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1541798100.0&et=1542065400.0', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1542065400.0&et=1542600000.0', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1542600000.0&et=1542867300.0', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1542867300.0&et=1543134600.0', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1543134600.0&et=1543669200.0', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1543669200.0&et=1544738400.0', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1544738400.0&et=1545807600.0', 'http://news.baidu.com/ns?word=重庆公交车坠江&bt=1545807600.0&et=1546876800.0']


    def getData(self,crawl_url):
        data = requests.get(crawl_url, headers=self.headers)
        html = data.text
        return html

    def hasNextPage(self, html):
        tree = etree.HTML(html)
        next_page = tree.xpath('//div[@id="wrapper"]/p[@id="page"]/a[contains(string(), "下一页")]/@href')
        if next_page != []:
            next_page_url = "http://news.baidu.com" + next_page[0]
        else:
            next_page_url = None
        return next_page_url

    def getResult(self, html):
        result = []
        tree = etree.HTML(html)
        temp_result = tree.xpath('//div[@id="content_left"]/div[3]//div[@class="result"]')
        for div in temp_result:
            temp = {
                'url' : None,
            }
            link = div.xpath('h3/a/@href')[0]
            temp['url'] = link

            result.append(temp)
        return result

    def run(self):
        totalurlnums = 0
        for url in self.fullResult:
            crawl_url = url
            print("[正在计算URL条数]%s" % crawl_url)
            while crawl_url != None:
                html = self.getData(crawl_url)
                result = self.getResult(html)
                totalurlnums  += len(result)
                crawl_url = self.hasNextPage(html)

        print("新闻总数为%d条" % totalurlnums)

if __name__ == "__main__":
    headers = {
        'Host': 'news.baidu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
    }

    search = CountBaiduUrls(headers)
    search.run()







