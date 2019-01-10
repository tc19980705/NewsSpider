from lxml import etree
import requests
import time

BaseUrl = "http://news.baidu.com/ns?word=%s&bt=%s&et=%s"
MaxSearchSize = 500

class BaiduNews(object):
    def __init__(self, keyword, headers, startTime, stopTime, target = None):
        self.keyword = keyword
        self.headers = headers
        self.target = target
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

    def makeUrl(self):
        searchUrls = []
        crawl_url = BaseUrl % (self.keyword, str(self.startTime), str(self.stopTime))

        print(crawl_url)

        html = self.getData(crawl_url)
        time.sleep(1)
        if BaiduNews.searchSize(html) > MaxSearchSize:
            medainTime = (self.stopTime + self.startTime) / 2

            searchUrls.append(BaiduNews.makeUrl(keyword, self.startTime, medainTime, self.headers))
            searchUrls.append(BaiduNews.makeUrl(keyword, medainTime, stopTime, self.headers))
        else:
            searchUrls.append(crawl_url)
        return searchUrls

    def getData(self, crawl_url):
        data = requests.get(crawl_url, headers=self.headers)
        html = data.text
        return html

    def getResult(self, html):
        result = []
        tree = etree.HTML(html)
        temp_result = tree.xpath('//div[@id="content_left"]/div[3]//div[@class="result"]')
        for div in temp_result:
            temp = {
                'url' : None,
                'title' : None
            }
            x_title = div.xpath('h3/a')[0]
            title = x_title.xpath('string(.)').strip('\n ')
            link = div.xpath('h3/a/@href')[0]
            temp['url'] = link
            temp['title'] = title

            result.append(temp)
        return result

    def saveData(self, result):
        if self.target == None:
            for i in result:
                print(i['url'], i['title'])
        #else:
            #target.add(result)

    def hasNextPage(self, html):
        tree = etree.HTML(html)
        next_page = tree.xpath('//div[@id="wrapper"]/p[@id="page"]/a[contains(string(), "下一页")]/@href')
        if next_page != []:
            next_page_url = "http://news.baidu.com" + next_page[0]
        else:
            next_page_url = None
        return next_page_url

    #def run(self):
        #crawl_url = self.makeUrl()
        #while crawl_url != None:
            #html = self.getData(crawl_url)
            #time.sleep(1)
            #result = self.getResult(html)
            #self.saveData(result)
            #crawl_url = self.hasNextPage(html)

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
        'Referer': 'http://news.baidu.com/ns?rn=20&ie=utf-8&cl=2&ct=1&bs=%E7%BA%A2%E9%BB%84%E8%93%9D%E5%B9%BC%E5%84%BF%E5%9B%AD&rsv_bp=1&sr=0&f=8&prevct=no&tn=news&word=%E7%BA%A2%E9%BB%84%E8%93%9D%E4%BA%B2%E5%AD%90%E5%9B%AD%E4%B8%BE%E8%A1%8C%E6%95%99%E5%B8%88%E9%9B%86%E4%B8%AD%E5%9F%B9%E8%AE%AD&rsv_sug3=3&rsv_sug4=238&rsv_sug1=1&rsv_sug2=0&inputT=10&rsv_sug=1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
    }
    keyword = u"重庆公交车坠江"

    search = BaiduNews(
        keyword,
        headers,
        "2018-10-01 00:00:00",
        "2019-01-08 00:00:00"
    )

    search.urls.append(search.makeUrl())
    singleResult = flat(search.urls)
    print(singleResult)







