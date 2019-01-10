#-*- coding utf-8 -*-
from goose3 import Goose
from goose3.text import StopWordsChinese
import requests
from lxml import etree
import DataBase
import pandas
import time
class NewsWebsite():
    def __init__(self,Baiduurl):
        self.Baiduurl = Baiduurl

    # def getSource(self):
    #     source_list = []
    #     for url in self.Baiduurl:
    #         req_header = {
    #             'User-Agent': 'Chrome',
    #             }
    #         req = requests.get(url, headers = req_header)
    #         req.encoding = 'utf-8'
    #         html = req.text
    #         tree = etree.HTML(html)
    #         source = tree.xpath('//div[@class="date-source"]/a/text()')
    #         source = ''.join(source)
    #         source_list.append(source)
    #     return source_list

    # def getTime(self):
    #     time_list = []
    #     for url in self.Baiduurl:
    #         req_header = {
    #             'User-Agent': 'Chrome',
    #             }
    #         req = requests.get(url, headers = req_header)
    #         req.encoding = 'utf8'
    #         html = req.text
    #         tree = etree.HTML(html)
    #         timedata = tree.xpath('//div[@class="date-source"]/span[@class="date"]/text()')
    #         timedata = ''.join(timedata)
    #         time_list.append(time)
    #     return time_list
    
    def gooseChineseExample(self):
        
        data_list = []
        # 文章地址
        #num = 0
        for url in self.Baiduurl:
            try:

                data_dict = {
                    'title' : None,
                    'url'   : None,
                    'text'  : None
                }
                data_dict['url'] = url
                # 初始化，设置中文分词
                g = Goose({'stopwords_class': StopWordsChinese})
                # 获取文章内容
                article = g.extract(url = url)
                # 获取标题
                title = article.title
                data_dict['title'] = title
                # 获取来源
                #source = self.getSource()
                #data_dict['sourse'] = str(source)
                # 发布时间
                #Time = self.getTime()
                #data_dict['time'] = str(Time)
                # 显示正文
                text = article.cleaned_text
                data_dict['text'] = text
                #num +=1

                data_list.append(data_dict)

                print(data_dict)

                time.sleep(0.1)

            except:
                continue;

        return data_list
    def run(self):
        self.gooseChineseExample()
        data_list = self.gooseChineseExample()
        print(data_list)
        try:
            #self.gooseChineseExample()
            #print(self.data_list)
             DataBase.MySqlDB().addtext(data_list)
             print('Successful!')
        except:
             print('Faile!')

             raise;


            

if __name__ == '__main__':
    db =DataBase.MySqlDB().connect
    sql1 = u"SELECT url FROM baidusearch;"
    #DataBase.MySqlDB().cursor.execute(sql1)
    t = pandas.read_sql(sql1,db).url.tolist()
    print(t)
    print(len(t))
    Baiduurl = t
    Website = NewsWebsite(Baiduurl)
    Website.run()
