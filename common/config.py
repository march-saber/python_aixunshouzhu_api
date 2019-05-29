import configparser
from common import contants

class ReadConfig:
    """完成配置文件读取"""

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(contants.global_file,encoding = 'utf-8') #加载global
        switch = self.config.getboolean('switch','on')
        if switch == True:
            self.config.read(contants.online_file,encoding = 'utf-8')
        elif switch == False:
            self.config.read(contants.test_file,encoding = 'utf-8')
        else:
            print("switch状态有误，请检查")

    def get(self,section,option):
        return self.config.get(section,option)

config = ReadConfig()
