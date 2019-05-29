#正则表达式

import re
import configparser
from common.config import config

class Context:
    load_id = None

def replace(data):
    p = '#(.*?)#'
    while re.search(p,data):     #从任意位置开始找，找到第一个就返回match object，如果没有就返回none
        #print(data)
        m = re.search(p,data)   #search查找匹配适合正则表达式的数据
        g = m.group(1)   #拿到参数化的key，只返回指定组里面的内容
        # g = m.group(0)   #返回表达式和组里面的内筒。#()#表示组

        try:
            v = config.get('data',g)   #根据key取到配置文件里面的值
        except configparser.NoOptionError as e:
            #类反射
            if hasattr(Context,g):
                v = getattr(Context,g)
            else:
                print("配置文件找不到参数化的值")
        print(v)
        data = re.sub(p,v,data,count=1)
    return data

