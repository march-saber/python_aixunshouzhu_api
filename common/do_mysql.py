import pymysql
from common.config import config

class DoMysql:
    """
    数据库的调用，完成MySQL数据库的交互
     """
    def __init__(self):
        host = '192.168.1.106'
        port = 3306
        user = "root"
        password = "root"
        # host = config.get('mysql','host')
        # prot = config.get('mysql','prot')
        # user = config.get('mysql','user')
        # password = config.get('mysql','user')

        self.mysql = pymysql.connect(host=host,port=port,user=user,password=password)
        self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)  #新建游标查询,括号内表示创建一个字典类型游标，返回的数据为字典

    def fetch_one(self,sql): #单个查询,编写sql语句并执行，查看结果
        self.cursor.execute(sql)   #执行sql语句
        #self.mysql.commit() #强制执行最新的
        return self.cursor.fetchone()  #返回获取查询结果集里面最近的一条数据，fetchone返回值为元祖

    def fetch_all(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()  #获取全部结果集

    def close(self):
        self.cursor.close()
        self.mysql.close()

if __name__ == '__main__':
    mysql = DoMysql()
    result = mysql.fetch_one("select max(mobilephone) from xrh.user")
    print(result)
    mysql.close()




