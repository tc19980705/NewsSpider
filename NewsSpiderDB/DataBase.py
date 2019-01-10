import pymysql;

class MySqlDB(object):
    def __init__(self):
        self.connect = None;
        self.cursor = None;
        try:
            self.connect = pymysql.connect(host = "localhost", user = "root", passwd = "1999211", db = "weibo", charset='utf8');
            self.cursor = self.connect.cursor();
            print("Successful!");
        except pymysql.Error as e:
            print(e.args[0], e.args[1]);
            print("Faile!");
            raise;

    def add(self,result):
        for i in result:
            try:

                sql2 = u"insert into baidusearch values('%s', '%s',0)" %(i['title'], (i['url']));
                self.cursor.execute(sql2.encode("utf-8"));
                self.connect.commit();
            except pymysql.Error as e:
                print(e.args[0], e.args[1]);
                print("Faile!");
                continue;
                raise;
    def addtext(self,data_list):
        for i in data_list:
            try:

                sql1 = u"insert into alltext values('%s', '%s','%s')" %(i['title'], i['url'],i['text']);
                self.cursor.execute(sql1.encode("utf-8"));
                self.connect.commit();
            except pymysql.Error as e:
                print(e.args[0], e.args[1]);
                print("Faile!");
                continue;
                raise;

# if __name__ == "__main__":
#     test = MySqlDB()
#     test.connect
#     test.add()
